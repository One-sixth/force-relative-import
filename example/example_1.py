from force_relative_import import enable_force_relative_import

with enable_force_relative_import():
    from .moduleA import return_good

print(return_good())
