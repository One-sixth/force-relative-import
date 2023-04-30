import os
import sys
import builtins
import functools
from contextlib import contextmanager

def _make_parent_str(level):
    if level == 0:
        r = ''
    else:
        r = '/..' * (level - 1)
    return r


def _force_relative_import_func(ori_import, info, name, globals=None, locals=None, fromlist=(), level=0):
    try:
        m = ori_import(name, globals, locals, fromlist, level)

    except ImportError as e:
        if e.msg != 'attempted relative import with no known parent package':
            # 不是目标异常，继续抛出
            raise e

        # 强制导入目标包
        require_module_file = globals['__file__']
        new_import_path = os.path.dirname(require_module_file) + _make_parent_str(level)
        sys.path.insert(0, new_import_path)
        m = ori_import(name)
        del sys.path[0]
        if info:
            print(f'Info! Force load relative module: {name} . Required by {require_module_file}', flush=True)

    return m


@contextmanager
def enable_force_relative_import(info=True):
    ori_import = builtins.__import__

    this_my_import = functools.partial(_force_relative_import_func, ori_import, info)

    # 变更import函数
    builtins.__import__ = this_my_import
    # 进入with作用域
    yield None
    # 离开with作用域
    # 恢复原来的import函数
    builtins.__import__ = ori_import


#
_global_ori_import = None


def global_enable_force_relative_import(info=True):
    global _global_ori_import

    if _global_ori_import is None:
        print('Info! The global force relative import function has been enabled! Only recommended for use in the main program, not in packages and modules!')
        _global_ori_import = builtins.__import__
        this_my_import = functools.partial(_force_relative_import_func, _global_ori_import, info)
        builtins.__import__ = this_my_import

    else:
        print('Info! The force relative import function has been enabled, and there is no need to enable it again.')


def global_disable_force_relative_import():
    global _global_ori_import

    if _global_ori_import is not None:
        print('Info! The global force relative import function has been disabled.')
        builtins.__import__ = _global_ori_import
        _global_ori_import = None

    else:
        print('Info! The global force relative import function is not enabled and does not need to be disable.')
