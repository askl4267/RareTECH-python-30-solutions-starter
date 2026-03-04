# Q01: String Split
# "apple,banana,orange"という文字列をカンマで分割してリストを作成し、表示してください。
text = "apple,banana,orange"
# ここにコードを書いてください
print(text.split(","))

# Q02: String Join
# ["Hello", "World", "Python"] というリストの要素をスペースで結合して、"Hello World Python" という文字列を作成し、表示してください。
words = ["Hello", "World", "Python"]
# ここにコードを書いてください
print(" ".join(words))

# Q03: Split and Join
# "one-two-three"という文字列をハイフンで分割し、アンダースコアで結合して "one_two_three" という文字列を作成し、表示してください。
sentence = "one-two-three"
print("_".join(sentence.split("-")))