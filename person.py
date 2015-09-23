__author__ = 'sci-lmw1'

from date import Date


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self, text):
        print("{} says {}".format(self.name, text))


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def speak(self, text):
        print("{} (ID {}) says {}".format(self.name, self.student_id, text))


p = Person("Joanne", 20)
p.speak("Good morning!")

s = Student("Kerry", 19, "123456")
s.speak("I study!")

