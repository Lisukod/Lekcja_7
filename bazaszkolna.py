from sys import argv
import re
phrase = argv[1]
students = []
teachers = []
hometeachers = []
allClassrooms = set()
class Uczen:
    def __init__(self, classroom):
        self.classroom = classroom
class Nauczyciel:
    def __init__(self, subject, classrooms = set()):
        self.subject = subject
        self.classrooms = classrooms
class Wychowawca:
    def __init__(self, homeroom):
        self. homeroom = homeroom
def assignClassrooms(room, allClassrooms):
    rooms = set()
    while room:
        rooms.add(room)
        room = input()
    allClassrooms.union(rooms)
    return rooms
while True:
    tempInput = input()
    if tempInput == "uczen":
        students.append(Uczen(input()))
    elif tempInput == "nauczyciel":
        teachers.append(Nauczyciel(input()))
        teachers[-1].classrooms.extend(assignClassrooms(input(), 
        allClassrooms))
    elif tempInput == "wychowawca":
        hometeachers.append(Wychowawca(input()))
        allClassrooms.add(hometeachers[-1].homeroom)
    else:
        break
if phrase in allClassrooms:
    for hometeacher in hometeachers:
        if hometeacher.homeroom == phrase: 
            print(hometeacher)
            break
    for student in students:
        if student.classroom == phrase:
            print(student)
elif re.match("hometeachers*", phrase) is not None:
    for student in students:
        if student.classroom == hometeachers[re.search("[.]", phrase)]:
            print(student)
elif re.match("teachers*", phrase) is not None:
    for hometeacher in hometeachers:
        if hometeacher.homeroom in teachers[re.search("[.]", 
        phrase)].classrooms:
            print(hometeacher)
elif re.match("students*", phrase) is not None:
    for student in students:
        pass
