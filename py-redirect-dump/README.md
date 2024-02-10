# redirect-dump

This is a simple example on how to redirect an internal `dump` function and
return the dumped value as a string.

## Usage

Run gdb and either use the redirect-dump.gdb file to load the extension, or do
so manually.  Run and break in `break_here` and call the new `$dump_arr` function.
The result should be:

```
$ DEBUGINFOD_URLS= gdb -x ./redirect-dump.gdb -ex run -ex 'printf "%s", $dump_arr(arr, len)' -ex c -ex quit ./redirect-dump
0: 0
1: 1
2: 2
3: 3
4: 4
5: 5
6: 6
7: 7
8: 8
9: 9
```
