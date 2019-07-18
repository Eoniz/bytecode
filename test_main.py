import dis
from pprint import pprint
import types

def a(a, *args, **kwargs):
    print(a)
    print(args)
    print(kwargs)

def c(a, *args):
    print(a)
    print(args)

def d(a):
    print(d)

def b():
    a(1, "b", "c", hello="world", foo="bar")


def fix(func, payload):
    fc_code = func.__code__

    co_consts = list(fc_code.co_consts)
    new_co_consts = co_consts
    store = { "hello": "foo", "world": "bar" }
    new_co_consts = (None, 1, 'b', 'c', 'world', 'bar', store, ('hello', 'foo', 'store'))
    new_payload = [116, 0, 100, 1, 100, 2, 100, 3, 100, 4, 100, 5, 100, 6, 100, 7, 141, 6, 1, 0, 100, 0, 83, 0]

    dis.dis(func.__code__)

    func.__code__ = types.CodeType(
        fc_code.co_argcount,
        fc_code.co_kwonlyargcount,
        fc_code.co_nlocals,
        fc_code.co_stacksize,
        fc_code.co_flags,
        bytes(new_payload),
        tuple(new_co_consts),
        fc_code.co_names,
        fc_code.co_varnames,
        fc_code.co_filename,
        fc_code.co_name,
        fc_code.co_firstlineno,
        fc_code.co_lnotab,
        fc_code.co_freevars,
        fc_code.co_cellvars
    )

    dis.dis(func.__code__)


b()
fix(b, b.__code__.co_code)
b()