# pretty-print

This is a simple example of a pretty printer for GDB in python.

# Usage

Run gdb and either use the pretty-print.gdb file to enable pretty printing and
load the extension, or do so manually.  Run and break in `use_list` and print it
with `print *list`.  The result should be:

```
$1 = 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9
```
