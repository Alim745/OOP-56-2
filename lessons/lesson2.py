# # Наследование
#
#
#
# # Родительский|Супер класс
# class Hero:
#
#     def __int__(self, name, lvl, age, hp):
#         self.name = name
#         self.lvl = lvl
#         self.age = age
#         self.hp = hp
#
#     def action(self):
#         return print(f"Base action")
#
# #
#
# # Дочерний класс
# class MageHero(Hero):
#
#
#     def __init__(self, name, lvl, age, hp, mp):
#         super().__int__(name, lvl, age, hp)
#         self.mp = mp
#
#     def rest(self):
#         return print(f"Я отдыхаю")
#
#
#     def action(self):
#         return print(f"========")
#
# hero = MageHero("Hero1", 100, 26, 1000, 100)
#
# hero.action()
#
#
# # ClassNameSomeThing - Верблюжья нотация(Camle case)
# # atribut_test_test - Змеиная нотация(Snake case)
#
# class Animal:
#     def action(self):
#         return print(f"Animal")
#
# class Swim(Animal):
#     def action(self):
#         return print(f"Swim")
#
# class Fly(Animal):
#     def action(self):
#         return print(f"Fly")
#
# class Duck(Fly, Swim):
#     pass
#
# donald_duck = Duck()
#
# print(Duck.mro())
# # mro - method resolution ordering
#
# # donald_duck.action()