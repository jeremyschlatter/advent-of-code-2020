import functools
import operator

from itertools import *

def product(xs):
    return functools.reduce(operator.mul, xs)
