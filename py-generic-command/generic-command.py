import gdb


class DumpCommand(gdb.Command):
    """Command to dump arrays and lists."""

    def __init__(self):
        """Create and register this command."""
        super(DumpCommand, self).__init__("dump", gdb.COMMAND_DATA)

    def dump_node(self, val):
        """Dump a value of type struct Node."""
        i = 0
        while val:
            print('{}: {}'.format(i, val['val']))
            val = val['next']

    def dump_array(self, val):
        """Dump a value of type struct Array."""
        for i in range(val['len']):
            print('{}: {}'.format(i, val['base'][i]))

    def invoke(self, val, from_tty):
        """Invoke this command."""
        val = gdb.parse_and_eval('{}'.format(val))
        base_type = val.type
        # resolve typedef
        if base_type.code == gdb.TYPE_CODE_TYPEDEF:
            base_type = base_type.strip_typedefs()
        # dereference potential pointer
        if base_type.code == gdb.TYPE_CODE_PTR:
            base_type = base_type.target()
            val = val.dereference()
        # call correct dump
        if base_type == gdb.lookup_type("struct Node"):
            self.dump_node(val)
        elif base_type == gdb.lookup_type("struct Array"):
            self.dump_array(val)
        else:
            raise gdb.error('Unsupported type {}'.format(str(base_type)))


# "Install" the command
DumpCommand()
