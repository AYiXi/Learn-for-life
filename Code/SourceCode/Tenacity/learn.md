```python
__str__   %s  :  print(f)   : string
__repr__  %r  :  f          : representation
repr(self)    : self.__repr__()

type(class).__name__  :  function.__name__
self.__class__ == type(self)

state_str = ', '.join('%s=%r' % (field, getattr(self, field)) for field in self.REPR_FIELDS)

a + b = a.__add__(b) = b.__radd__(a)  :  reverse

__call__  :  Class()
class Counter:
    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        return self.func(*args, **kwargs)

@Counter
def foo(a):
    return a


__slots__  : protect class attribute from modification 
```