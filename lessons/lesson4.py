# Магические методы
class Test:
    def __init__(self, name):
        self.name = name


    def __str__(self):
        return f"My method! {self.name}"

test = Test("Test")

print(test)



