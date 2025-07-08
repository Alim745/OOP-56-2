

class Hero:

    # Консструктор класса
    def __init__(self, name, lvl, hp):
        # Атрибуты класса
        self.name = name
        self.lvl = lvl
        self.hp = hp

    # Метод класса
    def introduce(self):
        return print(f"Привет меня зовут {self.name}")

# Объект|экзэмпляр класса
kirito = Hero("Kirito", "100", "1000")
asuna = Hero("Asuna", "10", "100")

kirito.introduce()
asuna.introduce()
print(kirito.name, kirito.lvl)
print(asuna.name, asuna.lvl)

some_text = "Some_text"

print(type(asuna))
print(type(some_text))