# prompt

An extension that shows how to hook the prompt.

## Usage

Run gdb and either use the prompt.gdb file to load the extension, or do so 
manually.  Break in `break_here` and select different frames with `frame`. The 
prompt will change and always show the name of the current frame.

```
$ DEBUGINFOD_URLS= gdb -q -x ./prompt.gdb -ex run  ./prompt
(gdb break_here) 
```
