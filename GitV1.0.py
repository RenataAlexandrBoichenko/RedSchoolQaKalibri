class Person:

    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def walk(self):
         return "I can walk"

    def hello(self):
        return f'Hello, my name is {self.name} {self.surname}'

    def set_name(self, new_name):
        self.name = new_name

    def get_name(self):
        return new_name

person_1 = Person('Renata', 'Boi', 30)
print(person_1.set_name('kati'))
print(person_1.age)
print(person_1.surname)
print(person_1.hello())
print(person_1.get_name())
print(person_1.walk())

person_2 = Person('Vadim', 'Boi')
print(person_2.name)
print(person_2.surname)
print(person_2.hello())
print(person_2.walk())

person_3 = Person('Arina', 'Boi')
print(person_3.name)
print(person_3.surname)
print(person_3.hello())
print(person_3.walk())

person_4 = Person('Solomeyi', 'Skladovckayi-Kuri')
print(person_4.name)
print(person_4.surname)
print(person_4.hello())
print(person_4.walk())

class Tester(Person):

    def __init__(self, name, surname, framework, age):
        super().__init__(name, surname, age)
        self.framework = framework

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
print(tester_1.age)

tester_2 = ManualTester('Renata', 'Boich', 'manual', 24)
print(tester_2.name)
print(tester_2.surname)
print(tester_2.framework)
print(tester_2.hello())
print(tester_2.test())
print(tester_2.age)
class Person:

    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age   #__age - скрытый и вывод будет _Person__age: