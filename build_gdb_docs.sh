#!/bin/sh

set -e
set -u
unset CDPATH
IFS='
	'

usage () {
    cat <<EOF
Usage: $(basename "$0") [-h] [-s] VERSION

Download the sources for the given GDB version and build the documentation.

Options:
  -s   Skip signature verification
  -h   Show this help and exit
EOF
}

VERSION=''
CHECK_SIG=1

while getopts ":hs" arg; do
    case "${arg}" in
        h)
            usage
            exit 0
            ;;
        s)
            CHECK_SIG=0
            ;;
        \?)
            printf >&2 'Illegal option -- %s\n' "$OPTARG"
            exit 1
            ;;
    esac
done
shift $((OPTIND-1))

if test "$#" -ne 1; then
    >&2 usage
    exit 1
fi
VERSION="$1"

if ! echo "${VERSION}" |grep -q '^[1-9][0-9]*\.[0-9]'; then
    printf >&2 'Illegal version "%s"\n' "${VERSION}"
    exit 1
fi

FILE_PATTERN='gdb-%s.tar.xz'
BASE_URL='https://ftp.gnu.org/gnu/gdb/'
FILE="$(printf "${FILE_PATTERN}" "${VERSION}")"
DIR="${FILE%.*}"
DIR="${DIR%.*}"
URL="$(printf "%s%s" "${BASE_URL}" "${FILE}")"

if test -e "${FILE}"; then
    printf 'GDB source file already exists: %s\n' "${FILE}"
    printf 'Skipping download\n'
else
    wget -- "${URL}"
fi

if test "${CHECK_SIG}" -eq 1; then
    if test -e "${FILE}.sig"; then
        rm -f -- "${FILE}.sig"
    fi
    wget -- "${URL}.sig"
    gpg --verify -- "${FILE}.sig"
fi

if test -e "${DIR}"; then
    printf 'GDB source directory already exists: %s\n' "${DIR}"
    printf 'Skipping unpacking\n'
else
    tar -xJf "${FILE}"
fi

cd "${DIR}/gdb"

./configure

make -C doc html MAKEINFO=makeinfo MAKEINFOFLAGS='--no-split' -j4

printf 'Done. Open with:\nxdg-open %s/gdb/doc/gdb.html\n' "${DIR}"
