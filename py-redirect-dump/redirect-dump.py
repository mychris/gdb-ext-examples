import gdb
import tempfile


class DumpArr(gdb.Function):
    """Dump an array"""

    def __init__(self):
        super(DumpArr, self).__init__("dump_arr")

    def invoke(self, arr, length):
        with tempfile.NamedTemporaryFile() as tmp:
            name = tmp.name
            s = gdb.parse_and_eval('(FILE*)fopen("{}", "w")'.format(name))
            gdb.parse_and_eval('fdump_arr({}, {}, {})'.format(s, arr, length))
            gdb.parse_and_eval('(int)fclose({})'.format(s))
            with open(name, 'r') as f:
                return f.read()


DumpArr()
