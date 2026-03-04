from datetime import datetime, timedelta

# Q1: `datetime`オブジェクトのフォーマット指定
# 2023年4月1日 15時30分00秒 を表すdatetimeオブジェクトを作成し、
# `strftime()` を使って "YYYY-MM-DD HH:MM:SS" の形式の文字列に変換して表示してください。
# ここにコードを書いてください
dt_obj = datetime(2023, 4, 1, 15, 30, 0)
print(dt_obj.strftime("%Y-%m-%d %H:%M:%S"))


# Q2: `timedelta` を使った日付の計算
# Q1で作成したdatetimeオブジェクトの7日後の日時を計算し、
# "YYYY-MM-DD HH:MM:SS" の形式の文字列に変換して表示してください。
# ここにコードを書いてください
delta = timedelta(days=7)
print(dt_obj + delta)