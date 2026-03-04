# 問１：数値を2倍しよう
# `original_numbers` の各要素を2倍にした新しいリスト `doubled_numbers` をリスト内包表記で作成してください。
original_numbers = [1, 2, 3, 4, 5]
# 以下に処理を記述してください
doubled_numbers = [num * 2 for num in original_numbers]
print(f"問1: {doubled_numbers}")

# 問２：偶数だけを取り出してみよう
# `mixed_numbers` から偶数だけを抽出した新しいリスト `even_numbers` をリスト内包表記で作成してください。
mixed_numbers = [1, 2, 3, 4, 5, 6]
# 以下に処理を記述してください
even_numbers = [num for num in mixed_numbers if num % 2 == 0]
print(f"問2: {even_numbers}")

# 問３：文字列の長さをリストにしてみよう
# `fruit_names` の各文字列の長さを要素とする新しいリスト `name_lengths` をリスト内包表記で作成してください。
fruit_names = ["apple", "banana", "cherry"]
# 以下に処理を記述してください
name_lengths = [len(name) for name in fruit_names]
print(f"問3: {name_lengths}")

# 問４：大文字に変換してみよう
# `lowercase_names` の各文字列を大文字に変換した新しいリスト `uppercase_names` をリスト内包表記で作成してください。
lowercase_names = ["alice", "bob", "charlie"]
# 以下に処理を記述してください
uppercase_names = [name.upper() for name in lowercase_names]
print(f"問4: {uppercase_names}")

# 問５：0〜9 の平方数リストを作成しよう
# 0から9までの数値の平方数を要素とするリスト `square_numbers` をリスト内包表記で作成してください。
# 以下に処理を記述してください
square_numbers = [num ** 2 for num in range(10)]
print(f"問5: {square_numbers}")

# 問6：条件付きで値を変えてみよう
# `scores` の各要素が10以上なら "OK"、そうでなければ "NG" となる新しいリスト `pass_fail_labels` をリスト内包表記で作成してください。
scores = [5, 12, 8, 20]
# 以下に処理を記述してください
pass_fail_labels = ["OK" if score >= 10 else "NG" for score in scores]
print(f"問6: {pass_fail_labels}")