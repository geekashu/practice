import random
import operator

class Student(object):
    def __init__(self, name, age, marks, rollNumber):
        self.name = name
        self.age = age
        self.marks = marks
        self.rollNumber = rollNumber

    def __str__(self):
        return "Name - {0}, Age - {1}, Marks - {2}, Roll Number - {3}".format(
            self.name, self.age, self.marks, self.rollNumber)



students = []
for x in range(100):
    students.append(Student(name="Student "+str(x), age=x*2, marks=x, rollNumber=x*10))

# Scramble our list
st_new = students[:]
random.shuffle(st_new)

for st in st_new:
    print(st)

print("---------Name--------")
# name
sorted_list_1 = sorted(st_new, key=operator.attrgetter('name'))

for st in sorted_list_1:
    print(st)

print("---------Name--------")
print("---------Age, Name--------")
sorted_list_2 = sorted(st_new, key=operator.attrgetter('age', 'name'))
for st in sorted_list_2:
    print(st)
print("---------Age, Name--------")
