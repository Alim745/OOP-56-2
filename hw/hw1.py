class Animal:
    def __init__(self, kingdom, phylum, class_name, order, family, genus, species):
        self.kingdom = kingdom
        self.phylum = phylum
        self.class_name = class_name
        self.order = order
        self.family = family
        self.genus = genus
        self.species = species
    def inroduce(self):
        print(f"Биологическая классификация:")
        print(f"Царство: {self.kingdom}")
        print(f"Тип: {self.phylum}")
        print(f"Класс: {self.class_name}")
        print(f"Отряд: {self.order}")
        print(f"Семейство: {self.family}")
        print(f"Род: {self.genus}")
        print(f"Вид: {self.species}")

Cat = Animal("Животные","Хордовые","Млекопитающие","Хищные","Кошачьи","Кошки","Домашняя кошки",)
Dog = Animal("Животные","Хордовые","Млекопитающие","Хищные","Псовые","Собаки","Домашняя собака",)
Cat.inroduce()
Dog.inroduce()