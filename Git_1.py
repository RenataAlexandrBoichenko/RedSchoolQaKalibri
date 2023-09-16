class Person:

    def __init__(self, name, surname, __age):
        self.name = name
        self.surname = surname
        # self.age = age
        self.__age = 1  # устанавливаем возраст

    def set_age(self, age):
        if 1 < age < 110:
            self.__age = age
        else:
            return "Недопустимый возраст"

    def get_age(self):
        return self.__age

    def display_info(self):
        return f"Имя: {self.name}\tВозраст: {self.__age}"

    def walk(self):
         return "I can walk"

    def hello(self):
        return f'Hello, my name is {self.name} {self.surname}'


person_1 = Person('Renata', 'Boi', 30)
print(person_1.surname)
print(person_1.hello())
print(person_1.walk())
print(person_1.display_info())  # Имя: Tom  Возраст: 1
print(person_1.set_age(-3486))  # Недопустимый возраст
print(person_1.set_age(25))
print(person_1.display_info())  # Имя: Tom  Возраст: 25
#
person_2 = Person('Vadim', 'Boi', 37)
print(person_2.name)
print(person_2.surname)
print(person_2.hello())
print(person_2.walk())

person_3 = Person('Arina', 'Boi', 3)
print(person_3.name)
print(person_3.surname)
print(person_3.hello())
print(person_3.walk())

person_4 = Person('Solomeyi', 'Skladovckayi-Kuri', 5)
print(person_4.name)
print(person_4.surname)
print(person_4.hello())
print(person_4.walk())

class Tester(Person):

    def __init__(self, name, surname, framework, age):
        super().__init__(name, surname, age)
        self.framework = framework
        self.__age = age

    def test(self):
        return "I love autotesting"


class ManualTester(Tester):

    def __init__(self, name, surname, framework, age):
        super().__init__(name, surname, framework, age)

tester_1 = Tester('Nikita', 'Gun', 'pythontest', 37)
print(tester_1.name)
print(tester_1.surname)
print(tester_1.framework)
print(tester_1.hello())
print(tester_1.test())
print(tester_1.get_age())

tester_2 = ManualTester('Renata', 'Boich', 'manual', 24)
print(tester_2.name)
print(tester_2.surname)
print(tester_2.framework)
print(tester_2.hello())
print(tester_2.test())
print(tester_2.get_age())

