import gdb


def example_prompt_hook(current_prompt):
    name = gdb.selected_frame().name()
    return '(gdb {}) '.format(name)


gdb.prompt_hook = example_prompt_hook
