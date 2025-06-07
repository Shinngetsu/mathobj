# mathobj
This module provides the "MathObj" class, which encapsulates the implementation of operator overrides.

## 特徴
- 演算子の処理をダンダーメソッドではなく、以下の３つのメソッドの実装によって定義できます
  - _unary : 単項演算
  - _binary : 二項演算
  - _rbinary : 二項演算(ただし第二引数として呼ばれた場合のみ)

## インストール
```
git clone https://github.com/Shinngetsu/mathobj.git
cd mathobj
pip install .
```

## 使い方
### 単純なベクトルの定義
```python
from mathobj import MathObj

class MyVector(MathObj):
  def __init__(self, x, y):
    self.x = x
    self.y = y
  def _unary(self, fn):
    return MyVector(fn(self.x), fn(self.y))
  def _binary(self, fn, b):
    if isinstance(b, MyVector):
      return MyVector(fn(self.x, b.x), fn(self.y, b.y))
    return MyVector(fn(self.x, b), fn(self.y, b))
  def _rbinary(self, fn, b):
    if isinstance(b, MyVector):
      return MyVector(fn(b.x, self.x), fn(b.y, self.y))
    return MyVector(fn(b, self.x), fn(b, self.y))
  def __str__(self):
    return f'MyVector({self.x:.2f}, {self.y:.2f})'

a = MyVector(10, 20)
b = MyVector(20, 30)
print(a + b) # MyVector(30, 50)
```
