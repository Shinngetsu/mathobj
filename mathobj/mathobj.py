#coding: utf-8
import operator as op, itertools as its, abc


unaries = (op.pos, op.neg, op.inv, op.abs)
'''単項演算'''
binaries = (op.add, op.sub, op.mul, op.truediv, op.floordiv, op.mod,
    op.and_, op.or_, op.xor, op.rshift, op.lshift, op.matmul,
    op.lt, op.gt, op.le, op.ge, op.eq, op.ne,)
'''二項演算'''
rjoins = (op.pow,)
'''右結合の演算子'''

def defop(local, o):
    name = o.__name__.replace('_', '')
    if o in unaries:
        local[f'__{name}__'] = lambda self: self._unary(o)
    else:
        local[f'__{name}__'] = lambda self, b: self._binary(o, b)
        local[f'__r{name}__'] = lambda self, a: self._rbinary(o, a)

class MathObj(abc.ABC):
    """演算子のオーバーライドを効率的に定義する"""
    @abc.abstractmethod
    def _unary(self, uf):
        """単項演算子の処理"""
    @abc.abstractmethod
    def _binary(self, bf, b):
        """二項演算子"""
    @abc.abstractmethod
    def _rbinary(self, bf, a):
        """二項演算子(逆)"""
    for o in its.chain(unaries, binaries): defop(locals(), o)
    del o
    def __hash__(self): return id(self)
