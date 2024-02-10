# gdb-ext-examples

This repository holds a small collection of sample gdb extensions.

## GDB documentation

The online documentation is only available for the latest release:

- [script extensions](https://sourceware.org/gdb/current/onlinedocs/gdb.html/Sequences.html#Sequences)
- [python extensions](https://sourceware.org/gdb/current/onlinedocs/gdb.html/Python.html#Python)
- [guile extensions](https://sourceware.org/gdb/current/onlinedocs/gdb.html/Guile.html#Guile)

If an older GDB version is used, one can build the documentation from source:

- `wget https://ftp.gnu.org/gnu/gdb/gdb-13.1.tar.xz`
- `tar -xJf gdb-13.1.tar.xz`
- `cd gdb-13.1/gdb/`
- `./configure`
- `make -C doc html MAKEINFO=makeinfo MAKEINFOFLAGS='--no-split' -j4`
- `xdg-open doc/gdb.html`

See the `build_gdb_docs.sh` script.

## License

Unlicense / Public domain
