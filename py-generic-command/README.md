# generic-command

This simple example shows how to implement a command which acts on different
types.  It can receive the defined `Array` or `List` type as value or as pointer
and dumps their contents.

## Usage

Run gdb and either use the generic-command.gdb file to load the extension, or do
so manually.  Run and break in `break_here` and call the new command `dump`.
The result should be:

```
$ DEBUGINFOD_URLS= gdb -x ./generic-command.gdb -ex run -ex 'dump(array)' -ex 'dump(*list)' -ex c -ex quit ./generic-command
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
0: 0
0: 1
0: 2
0: 3
0: 4
0: 5
0: 6
0: 7
0: 8
0: 9
```
