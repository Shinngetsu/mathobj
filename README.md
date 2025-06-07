# mathobj
This module provides the "MathObj" class, which encapsulates the implementation of operator overrides.

## 特徴
- 演算子の処理をダンダーメソッドではなく、以下の３つのメソッドの実装だけで定義できます
  - _unary : 単項演算
  - _binary : 二項演算
  - _rbinary : 二項演算(ただし第二引数として呼ばれた場合のみ)
- 完全なスタンドアロン
  - Python標準モジュールのみに依存しています
- 処理能力はお察し

## インストール
```
git clone https://github.com/Shinngetsu/mathobj.git
cd mathobj
pip install .
```

## 使い方
単純なベクトルの定義
```python
from mathobj import MathObj

# 定義
class MyVector(MathObj):
  def __init__(self, x, y):
    self.x = x
    self.y = y
  def __str__(self):
    return f'MyVector({self.x:.2f}, {self.y:.2f})'

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
  
# 使用
a = MyVector(10, 20)
b = MyVector(20, 30)
print(a + b) # MyVector(30, 50)
```
### _unary()メソッドに渡される関数
|関数|表記
|-------------|---------------
|operator.pos|+obj
|operator.neg|-obj
|operator.inv|~obj
|operator.abs|abs(obj)

### _binary(), _rbinary()メソッドに渡される関数
|関数|表記
|-------------|---------------
|operator.add|a + b
|operator.sub|a - b
|operator.mul|a * b
|operator.truediv|a / b
|operator.floordiv|a // b
|operator.mod|a % b
|operator.and_|a & b
|operator.or_|a \| b
|operator.xor|a ^ b
|operator.rshift|a >> b
|operator.lshift|a << b
|operator.matmul|a @ b
|operator.lt|a < b
|operator.gt|a > b
|operator.le|a <= b
|operator.ge|a >= b
|operator.eq|a == b
|operator.ne|a != b

## 必要条件
- Python 3.13.1 (動作確認済)


