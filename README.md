# gdb-ext-examples

This repository holds a small collection of sample gdb extensions.

## Structure

Each sample extension is self-contained and in its own sub-directory.

For each extension, there is a sample C application which can be used
to try it out.  A `MAKEFILE` is provided to build the appliction. The
`README.md` file gives a short introduction on how to use the
extension.  There is a `*.gdb` file which can be used to load the
extension and configure GDB for it (if this is required).  Usually,
each application has a function called `break_here` in which a
breakpoint can be set.  The `*.gdb` file should do this already.
Start GDB with the provided command line.

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
