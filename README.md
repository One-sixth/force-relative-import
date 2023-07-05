# force-relative-import
This is a library that forcibly enables Python relative import, allowing you to ignore Python's relative import restrictions.  
这是一个强制启用python相对导入的库，允许你忽略python的相对导入限制。  


# Install / 安装
```shell
pip install -U force-relative-import
```


# Usage Method / 使用方法

## Method 1 (Recommend) / 方法1 (推荐)
Use scopes to avoid unexpected situations.  
使用作用域，以避免意外情况。  

[example_1.py](example/example_1.py)
```python
from force_relative_import import enable_force_relative_import

with enable_force_relative_import():
    from .moduleA import return_good

print(return_good())

```

[example_4.py](example/example_4/example_4.py)
```python
from force_relative_import import enable_force_relative_import

with enable_force_relative_import():
    from ..moduleA import return_good

print(return_good())

```

[example_5.py](example/example_4/example_5/example_5.py)
```python
from force_relative_import import enable_force_relative_import

with enable_force_relative_import():
    from ...moduleA import return_good

print(return_good())

```


## Method 2 / 方法2
Using functions.  
使用函数。  

[example_2.py](example/example_2.py)
```python
from force_relative_import import enable_force_relative_import, global_enable_force_relative_import, global_disable_force_relative_import

global_enable_force_relative_import()

from .moduleA import return_good

global_disable_force_relative_import()

print(return_good())

```


## Method 3 / 方法3
Recommended only for main programs, not for modules or packages.  
仅建议用于主程序，不要用于模块或包。  

[example_3.py](example/example_3.py)
```python
from force_relative_import import enable_now

from .moduleA import return_good

print(return_good())


```
