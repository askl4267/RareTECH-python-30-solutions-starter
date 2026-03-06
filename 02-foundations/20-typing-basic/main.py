from typing import List

# Q01: Type Hints for Variables
# 文字列 "Alice" を保持する変数 `name` と、整数 20 を保持する変数 `age` に型ヒントを付けて定義し、
# f-string を使って "Alice is 20 years old" と表示してください。
# ここにコードを書いてください
name: str = "Alice"
age: int = 20
print(f"{name} is {age} years old")

# Q02: Type Hints for Functions
# 2つの整数 `a` と `b` を受け取り、その合計を返す `add` 関数に型ヒントを付けて定義してください。
# この関数を 5 と 3 を引数にして呼び出し、結果を表示してください。
# ここにコードを書いてください
def add(a: int, b: int) -> int:
    return a + b
print(add(5, 3))

# Q03: Type Hints for Lists
# 整数のリスト `[1, 2, 3, 4, 5]` を保持する変数 `numbers` に型ヒントを付けて定義してください。
# `sum()` 関数を使ってリストの合計を計算し、表示してください。
# ここにコードを書いてください
numbers: List[int] = [1, 2, 3, 4, 5]
print(sum(numbers))