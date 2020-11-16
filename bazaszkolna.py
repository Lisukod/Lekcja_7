from sys import argv
phrase = argv[1]
students = []
teachers = []
hometeachers = []
classrooms = []
class Uczen:
    def __init__(self, classroom):
        self.classroom = classroom
class Nauczyciel:
    def __init__(self, subject, classrooms):
        self.subject = subject
        self.classrooms = classrooms
class Wychowawca:
    def __init__(self, classrooms):
        self. classrooms = classrooms
while True:
    tempInput = input()
    if tempInput == "uczen":
        students.append(Uczen(input()))
    elif tempInput == "nauczyciel":
        teachers.append(Nauczyciel(input(), input()))