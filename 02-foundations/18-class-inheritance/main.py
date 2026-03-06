# Q01: Base Class
# "Dog" という名前で Animal クラスのインスタンスを作成し、
# speak() メソッドを呼び出して結果を表示してください。
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound"
# ここにコードを書いてください
print(Animal("Dog").speak())

# Q02: Inheritance
# Animal クラスを継承した Dog クラスを定義してください。
# speak() メソッドをオーバーライドして、"{name} barks" を返すようにしてください。
# "Buddy" という名前で Dog クラスのインスタンスを作成し、
# speak() メソッドを呼び出して結果を表示してください。
# ここにコードを書いてください
class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        return f"{self.name} barks"

print(Dog("Buddy").speak())

# Q03: Multiple Inheritance
# Animal クラスを継承した Cat クラスを定義してください。
# speak() メソッドをオーバーライドして、"{name} meows" を返すようにしてください。
# さらに、"{name} purrs" を返す purr() メソッドを追加してください。
# "Whiskers" という名前で Cat クラスのインスタンスを作成し、
# speak() と purr() メソッドを呼び出して結果を表示してください。
# ここにコードを書いてください

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        return f"{self.name} meows"
    
    def purr(self):
        return f"{self.name} purrs"

print(Cat("Whiskers").speak())
print(Cat("Whiskers").purr())