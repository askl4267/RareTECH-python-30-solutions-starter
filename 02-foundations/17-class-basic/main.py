# 問２：インスタンスを作成してみよう
# person.py の Person クラスをインポートし、
# 名前 "次郎"、年齢 20 でインスタンスを作成してください。
# そのインスタンスを使って say_hello() と introduce() メソッドを呼び出してください。
# 以下に処理を記述してください
from person import Person
from rectangle import Rectangle

jiro = Person("次郎", 20)
jiro.say_hello()
jiro.introduce()

# 問４：戻り値を出力しよう
# rectangle.py の Rectangle クラスをインポートし、
# 幅 3、高さ 4 でインスタンスを作成してください。
# area() メソッドを呼び出して面積を計算し、
# "辺の長さが...と...の四角の面積は...です" の形式で表示してください。
# 以下に処理を記述してください
shape = Rectangle(3, 4)
print(f"辺の長さが{shape.width}と{shape.height}の四角の面積は{shape.area()}です")