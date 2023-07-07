# 🐍 Python Tricks
---
---
[🐍PyTricks]: 
```python

```
---
[🐍PyTricks]: 
```python

```
---
[🐍PyTricks]: 
```python
# You can get the name of
# an object's class as a
# string:

>>> class MyClass: pass

>>> obj = MyClass()
>>> obj.__class__.__name__
'MyClass'

# Functions have a
# similar feature:

>>> def myfunc(): pass

>>> myfunc.__name__
'myfunc'
```
---
[🐍PyTricks]: Working with IP addresses in Python 3
```python
# Python 3 has a std lib
# module for working with
# IP addresses:

>>> import ipaddress

>>> ipaddress.ip_address('192.168.1.2')
IPv4Address('192.168.1.2')

>>> ipaddress.ip_address('2001:af3::')
IPv6Address('2001:af3::')

# Learn more here:
# https://docs.python.org/3/library/ipaddress.html
```
---
[🐍PyTricks]: Lambda Functions
```python
# The lambda keyword in Python provides a
# shortcut for declaring small and 
# anonymous functions:

>>> add = lambda x, y: x + y
>>> add(5, 3)
8

# You could declare the same add() 
# function with the def keyword:

>>> def add(x, y):
...     return x + y
>>> add(5, 3)
8

# So what's the big fuss about?
# Lambdas are *function expressions*:
>>> (lambda x, y: x + y)(5, 3)
8

# • Lambda functions are single-expression 
# functions that are not necessarily bound
# to a name (they can be anonymous).

# • Lambda functions can't use regular 
# Python statements and always include an
# implicit `return` statement.
```
---
[🐍PyTricks]: @classmethod vs @staticmethod vs "plain" methods
```python
# @classmethod vs @staticmethod vs "plain" methods
# What's the difference?

class MyClass:
    def method(self):
        """
        Instance methods need a class instance and
        can access the instance through `self`.
        """
        return 'instance method called', self

    @classmethod
    def classmethod(cls):
        """
        Class methods don't need a class instance.
        They can't access the instance (self) but
        they have access to the class itself via `cls`.
        """
        return 'class method called', cls

    @staticmethod
    def staticmethod():
        """
        Static methods don't have access to `cls` or `self`.
        They work like regular functions but belong to
        the class's namespace.
        """
        return 'static method called'

# All methods types can be
# called on a class instance:
>>> obj = MyClass()
>>> obj.method()
('instance method called', <MyClass instance at 0x1019381b8>)
>>> obj.classmethod()
('class method called', <class MyClass at 0x101a2f4c8>)
>>> obj.staticmethod()
'static method called'

# Calling instance methods fails
# if we only have the class object:
>>> MyClass.classmethod()
('class method called', <class MyClass at 0x101a2f4c8>)
>>> MyClass.staticmethod()
'static method called'
>>> MyClass.method()
TypeError: 
    "unbound method method() must be called with MyClass "
    "instance as first argument (got nothing instead)"
```
---
[🐍PyTricks]: Peeking Behind The Bytecode Curtain
```python
# You can use Python's built-in "dis"
# module to disassemble functions and
# inspect their CPython VM bytecode:

>>> def greet(name):
...     return 'Hello, ' + name + '!'

>>> greet('Dan')
'Hello, Dan!'

>>> import dis
>>> dis.dis(greet)
2   0 LOAD_CONST     1 ('Hello, ')
    2 LOAD_FAST      0 (name)
    4 BINARY_ADD
    6 LOAD_CONST     2 ('!')
    8 BINARY_ADD
   10 RETURN_VALUE
```
---
# [🐍PyTricks]: When To Use __repr__ vs __str__?
```python
# When To Use __repr__ vs __str__?
# Emulate what the std lib does:
>>> import datetime
>>> today = datetime.date.today()

# Result of __str__ should be readable:
>>> str(today)
'2017-02-02'

# Result of __repr__ should be unambiguous:
>>> repr(today)
'datetime.date(2017, 2, 2)'

# Python interpreter sessions use 
# __repr__ to inspect objects:
>>> today
datetime.date(2017, 2, 2)
```
---
# [🐍]: itertools.permutations()
```python
# itertools.permutations() generates permutations 
# for an iterable. Time to brute-force those passwords ;-)

>>> import itertools
>>> for p in itertools.permutations('ABCD'):
...     print(p)

('A', 'B', 'C', 'D')
('A', 'B', 'D', 'C')
('A', 'C', 'B', 'D')
('A', 'C', 'D', 'B')
('A', 'D', 'B', 'C')
('A', 'D', 'C', 'B')
('B', 'A', 'C', 'D')
('B', 'A', 'D', 'C')
('B', 'C', 'A', 'D')
('B', 'C', 'D', 'A')
('B', 'D', 'A', 'C')
('B', 'D', 'C', 'A')
('C', 'A', 'B', 'D')
('C', 'A', 'D', 'B')
('C', 'B', 'A', 'D')
('C', 'B', 'D', 'A')
('C', 'D', 'A', 'B')
('C', 'D', 'B', 'A')
('D', 'A', 'B', 'C')
('D', 'A', 'C', 'B')
('D', 'B', 'A', 'C')
('D', 'B', 'C', 'A')
('D', 'C', 'A', 'B')
('D', 'C', 'B', 'A')
```
---
# [🐍]: Finding the most common elements in an iterable
```python
# collections.Counter lets you find the most common
# elements in an iterable:

>>> import collections
>>> c = collections.Counter('helloworld')

>>> c
Counter({'l': 3, 'o': 2, 'e': 1, 'd': 1, 'h': 1, 'r': 1, 'w': 1})

>>> c.most_common(3)
[('l', 3), ('o', 2), ('e', 1)]
```


---
# [🐍PyTricks]: Python list slice syntax fun:
```python
# Python's list slice syntax can be used without indices
# for a few fun and useful things:

# You can clear all elements from a list:
>>> lst = [1, 2, 3, 4, 5]
>>> del lst[:]
>>> lst
[]

# You can replace all elements of a list
# without creating a new list object:
>>> a = lst
>>> lst[:] = [7, 8, 9]
>>> lst
[7, 8, 9]
>>> a
[7, 8, 9]
>>> a is lst
True

# You can also create a (shallow) copy of a list:
>>> b = lst[:]
>>> b
[7, 8, 9]
>>> b is lst
False
```
---
# [🐍PyTricks]: Python 3.5+ type annotations
```python
# Python 3.5+ supports 'type annotations' that can be
# used with tools like Mypy to write statically typed Python:

def my_add(a: int, b: int) -> int:
    return a + b
```
---
# [🐍PyTricks]: Different ways to test multiple flags at once in Python
```python 
# Different ways to test multiple
# flags at once in Python
x, y, z = 0, 1, 0

if x == 1 or y == 1 or z == 1:
    print('passed')

if 1 in (x, y, z):
    print('passed')

# These only test for truthiness:
if x or y or z:
    print('passed')

if any((x, y, z)):
    print('passed')
```

# [🐍PyTricks]: Merging two dicts in Python 3.5+ with a single expression

```python 
# How to merge two dictionaries
# in Python 3.5+

>>> x = {'a': 1, 'b': 2}
>>> y = {'b': 3, 'c': 4}

>>> z = {**x, **y}

>>> z
{'c': 4, 'a': 1, 'b': 3}

# In Python 2.x you could
# use this:
>>> z = dict(x, **y)
>>> z
{'a': 1, 'c': 4, 'b': 3}

# In these examples, Python merges dictionary keys
# in the order listed in the expression, overwriting 
# duplicates from left to right.
#
# See: https://www.youtube.com/watch?v=Duexw08KaC8
```
---
[🐍PyTricks]: Dicts can be used to emulate switch/case statements
```python 
# Because Python has first-class functions they can
# be used to emulate switch/case statements

def dispatch_if(operator, x, y):
    if operator == 'add':
        return x + y
    elif operator == 'sub':
        return x - y
    elif operator == 'mul':
        return x * y
    elif operator == 'div':
        return x / y
    else:
        return None


def dispatch_dict(operator, x, y):
    return {
        'add': lambda: x + y,
        'sub': lambda: x - y,
        'mul': lambda: x * y,
        'div': lambda: x / y,
    }.get(operator, lambda: None)()


>>> dispatch_if('mul', 2, 8)
16

>>> dispatch_dict('mul', 2, 8)
16

>>> dispatch_if('unknown', 2, 8)
None

>>> dispatch_dict('unknown', 2, 8)
None
 ```
 ---
# [🐍PyTricks]: Functions are first-class citizens in Python
 
 ```python 
 # Functions are first-class citizens in Python:

# They can be passed as arguments to other functions,
# returned as values from other functions, and
# assigned to variables and stored in data structures.

>>> def myfunc(a, b):
...     return a + b
...
>>> funcs = [myfunc]
>>> funcs[0]
<function myfunc at 0x107012230>
>>> funcs[0](2, 3)
5
 ```
---
# [🐍PyTricks]: Python's built-in HTTP server
 
 ```python 
 # Python has a HTTP server built into the
# standard library. This is super handy for
# previewing websites.

# Python 3.x
$ python3 -m http.server

# Python 2.x
$ python -m SimpleHTTPServer 8000

# (This will serve the current directory at
#  http://localhost:8000)
 ```
 ---
 # [🐍PyTricks]: Python's logging module
 ```python=
 import logging 

# Create and configure logger
LOG_FORMAT = "%(Levelname)s %(asctime)s %(message)s"
logging.basicConfig(filename = "./module_name.Log",
					level = logging.DEBUG,
					# Possibilities: DEBUG, INFO, WARNING, ERROR, CRITICAL
					format = LOG_FORMAT,
					filemode = 'w')

logger = logging.getLogger()

# Test the logger
logger.info("Our first message.")

# Display Log-Level
print(log.level)

# Test messages
logger.debug("This is a harmless debug message.")
logger.info("Just some useful info")
logger.warning("I'm sorry, but I can't do that Dave.")
logger.error("Did you just try to devide by zero?")
logger.critical("The entire internet is down!!")
```
