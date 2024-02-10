# tree-tui

A sample extension which provides a TUI window that renders the first tree found
in the current frame.

## Usage

Run gdb and either use the tree-tui.gdb file to load the extension, or do so manually.
Breaking in main and stepping through it will show how the tree is build.  Breaking in
`break_here` will show the full tree.

A new TUI layout needs to be created like `tui new-layout tree tree 1 cmd 1`.
Then, switch to the new layout with `layout tree`.  The tree-tui.gdb file
will do that and sets breakpoints in `main` and `break_here`.

Example output:

```
$ DEBUGINFOD_URLS= gdb -x ./tree-tui.gdb -ex run -ex continue ./tree-tui
└── Root
  ├── Child
  │  ├── Grandchild
  │  ├── Grandchild
  │  ├── Grandchild
  │  ├── Grandchild
  │  ├── Grandchild
  │  ├── Grandchild
  │  └── Grandchild
  ├── Child
```
