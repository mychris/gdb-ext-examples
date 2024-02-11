# hidden-break

A simple extension which defines a hidden breakpoint that collects the version
of the application and stores it for later use.  This extension provides a
GDB function called `version` which can be used to retrieve the application
version.

This might be usefull if a GDB extension needs to support multiple versions of
an application and needs to change behavior for older versions.

## Usage

Run gdb and either use the hidden-break.gdb file or load the extension manually.
Run and break in `break_here` and query the application version with
`call $version()`.  The result should be:

```
$ DEBUGINFOD_URLS= gdb -q --batch -x ./hidden-break.gdb -ex run -ex 'call $version()' ./hidden-break
$1 = "1.2.3"
```

If the inferior is stopped in `main()`, the version will no yet be available,
because the hidden breakpoint is set in `init()`.
