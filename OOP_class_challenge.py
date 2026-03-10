"""
Design a parent class called CFGStudent.

It should have general attributes like name, surname, age, email, student id
and methods to fetch student’s full name and student’s id.

Design a child class called NanoStudent, which  inherits from CFGStudent class.
This class should have exactly the same attributes as its parent class,
as well as an additional one called ‘specialization’ and course grades.

The child class ‘generate_id’ method should override its parent method to add the suffix ‘NANO’
in front of the id.

New methods ‘add_new_grade’ and ‘get_course_grades’ should be added.
You can use  it as a skeleton code for your classes OR adjust it and create your own.

"""

import random

class CFGStudent:

    def __init__(self, name, surname, age, email, student_id=None):
        self.name = name
        self.surname = surname
        self.age = age
        self.email = email
        self.student_id = student_id or self.generate_id()

    @staticmethod
    def generate_id():
        random_id = random.randrange(1000, 10000)
        return str(random_id)

    def get_id(self):
        return self.student_id

    def get_fullname(self):
        return f"{self.name} {self.surname}"


class NanoStudent(CFGStudent):

    def __init__(self, specialization, **kwargs):
        super().__init__(**kwargs)
        self.specialization = specialization
        self.course_grades = dict()

    @staticmethod
    def generate_id():
        random_id = random.randrange(1000, 10000)
        return f"NANO{random_id}"

    def add_new_grade(self, task_name, grade):
        self.course_grades[task_name] = grade

    def get_course_grades(self):
        return self.course_grades

# Example run

s = CFGStudent('Anna', 'Smith', 18, 'anna@mail.com')  # do not pass ID, it should be generated automatically
print(s.get_fullname())
# returns 'Anna Smith'
print(s.student_id)
# returns '3868' or some other random number

cfg_s = NanoStudent('Software', name='Mia', surname='Papandopulu', age=20, email='mia@mail.com')
print(cfg_s.get_fullname())
# returns 'Mia Papandopulu'
print(cfg_s.get_id())
# returns 'NANO6180' or some other random number

cfg_s.add_new_grade('theory', 95)
cfg_s.add_new_grade('project', 78)
print(cfg_s.get_course_grades())
# returns {'theory': 95, 'project': 78}