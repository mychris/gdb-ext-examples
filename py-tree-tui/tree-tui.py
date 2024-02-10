import gdb


class TreeTui:
    """A TUI window showing the first Node found on the stack"""
    def __init__(self, window):
        # The current TUI window
        self.__window = window
        self.__window.title = 'Tree View'
        # The tree node found in __on_stop
        self.__tree = None
        # vertical position for scrolling
        self.__vpos = 0
        # horizontal position for scrolling
        self.__hpos = 0
        # content holding the whole tree as a string
        self.__content = ''
        # current line while rendering
        self.__current_line = 0
        # Create an event listener, which triggers rendering and
        # discovers the tree
        gdb.events.before_prompt.connect(self.__on_stop)

    def __on_stop(self):
        """Callback which searches for a Node object and renders the window"""
        self.__tree = None
        frame = gdb.selected_frame()
        try:
            block = frame.block()
        except RuntimeError:
            # Can happen if there are no debugging information
            return
        # Go through all the blocks until a Node is found
        while not self.__tree and block:
            # Go through this block and search for a Node
            for x in block:
                if not x.is_valid():
                    continue
                typ = x.type.strip_typedefs()
                try:
                    val = x.value(frame)
                except Exception:
                    continue
                if typ.code == gdb.TYPE_CODE_PTR:
                    if val and typ.target() == gdb.lookup_type("struct Node"):
                        self.__tree = val.dereference()
                        break
            block = block.superblock
        # Always render again!
        self.render()

    def close(self):
        """Callback for window close event, disconnect the even listener"""
        gdb.events.before_prompt.disconnect(self.__on_stop)

    def vscroll(self, amount):
        """Callback when the user scrolls vertically"""
        self.__vpos = max(0, self.__vpos + amount)
        # Always render again!
        self.render()

    def hscroll(self, amount):
        """Callback when the user scrolls horizontally"""
        self.__hpos = max(0, self.__hpos + amount)
        # Always render again!
        self.render()

    def __render_line(self, content):
        """Render a single line, handles scroll position and width/height"""
        self.__current_line += 1
        if self.__current_line > self.__window.height + self.__vpos:
            return
        if self.__current_line <= self.__vpos:
            return
        content = content[self.__hpos:]
        content = content[:self.__window.width]
        self.__content += content + '\n'

    def __render(self, tree, last, header):
        """Render the tree recursively"""
        header_line = header
        header_line += '└── ' if last else '├── '
        try:
            header_line += tree['name'].string()
        except gdb.MemoryError:
            return
        self.__render_line(header_line)
        try:
            children = [tree['childs'][i] for i in range(10) if tree['childs'][i]]
        except gdb.MemoryError:
            children = []
        for i in range(len(children)):
            next_header = '   ' if last else '│  '
            next_last = (i == len(children) - 1)
            self.__render(tree['childs'][i], next_last, header + next_header)

    def render(self):
        """Render window callback"""
        self.__content = ''
        self.__current_line = 0
        self.__window.erase()
        if self.__tree:
            self.__render(self.__tree, True, '')
            self.__window.write(self.__content)
        else:
            self.__window.write('\n\n')
            self.__window.write("No tree found".center(self.__window.width))
            self.__window.write('\n')


# Register the new TUI window
gdb.register_window_type("tree", TreeTui)
