from force_relative_import import enable_force_relative_import, global_enable_force_relative_import, global_disable_force_relative_import

global_enable_force_relative_import()

with enable_force_relative_import():
    from .moduleA import return_good

global_disable_force_relative_import()

print(return_good())
