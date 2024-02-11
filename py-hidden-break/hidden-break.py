import gdb

VERSION = None


class CollectVersionBreakpoint(gdb.Breakpoint):
    """A temporary invisible breakpoint which collects the version
    of the application"""

    def __init__(self):
        super(CollectVersionBreakpoint, self).__init__(spec="init",
                                                       type=gdb.BP_BREAKPOINT,
                                                       internal=True,
                                                       temporary=True)

    def stop(self):
        """Callback triggered when the breakpoint is hit.
        Return False to make the inferior continue automatically."""
        global VERSION
        VERSION = gdb.parse_and_eval("VERSION").string()
        return False


class Version(gdb.Function):
    """Function returning the current version of the application."""

    def __init__(self):
        super(Version, self).__init__("version")

    def invoke(self):
        return VERSION if VERSION else ""


Version()
CollectVersionBreakpoint()
