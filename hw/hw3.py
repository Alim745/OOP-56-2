class Student:

    def __init__(self, name, _grade, __password):
        self.name = name
        self._grade = _grade
        self.__password = __password

    def change_password(self, new_pass):
        self.__password = new_pass

    def get_info(self):
        return print(f"Name: {self.name}, Grade: {self._grade}")


s1 = Student("Alim", "5", "123321")

s1.change_password("321123")
s1.get_info()


from abc import ABC, abstractmethod

class Vechile(ABC):

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def stop(self):
        pass



class Car(Vechile):

    def move(self):
        pass

    def stop(self):
        pass



class Bike(Vechile):

    def move(self):
        pass

    def stop(self):
        pass

car = Car()
bike = Bike()

car.move()
car.stop()
bike.move()
bike.stop()