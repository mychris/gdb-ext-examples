from gdb.printing import RegexpCollectionPrettyPrinter, register_pretty_printer


class ListPrinter:
    """Pretty Printer for the List"""

    def __init__(self, value):
        self.__value = value

    def to_string(self):
        result = str(self.__value['i'])
        val = self.__value['next']
        while val:
            result += ' -> '
            result += str(val['i'])
            val = val['next']
        return result


# Create a printer collection with the name gdb-ext-examples
package_pretty_printers = RegexpCollectionPrettyPrinter("gdb-ext-examples")
# Register the collection for pretty printing
register_pretty_printer(None, package_pretty_printers)
# Add the ListPrinter to the collection
# Make sure to use the correct type for the regex
# Use `ptype` in gdb to find it.
# Or `python print(gdb.selected_frame().read_var("<variable name>").type.name)`
package_pretty_printers.add_printer("List", "^Node$", ListPrinter)
