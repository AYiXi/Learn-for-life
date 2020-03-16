def arglist_to_dict(arglist):
    """Convert a list of arguments like ['arg1=val1', 'arg2=val2', ...] to a
    dict
    """
    """
    dict() -> new empty dictionary
    dict(mapping) -> new dictionary initialized from a mapping object's
        (key, value) pairs
    NOTE dict(iterable) -> new dictionary initialized as if via:
        d = {}
        for k, v in iterable:
            d[k] = v
    dict(**kwargs) -> new dictionary initialized with the name=value pairs
        in the keyword argument list.  For example:  dict(one=1, two=2)
    # (copied from class doc)
    """
    # NOTE x.split('=', maxsplit=1)
    return dict(x.split('=', 1) for x in arglist)

# NOTE 
{'arg1': 'val1', 'arg2': 'val2'}.pop('arg1', True) == 'val1' or True

# AssertionError, Warning, TypeError 断言错误, 警告, 类型错误