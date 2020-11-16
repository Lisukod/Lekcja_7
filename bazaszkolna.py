from sys import argv

classDict = {}
teacherDict = {}
phrase = argv[1]


class Klasa:
    def __init__(self, students=set(), hometeacher=""):
        self.students = students
        self.hometeacher = hometeacher


class Nauczyciel:
    def __init__(self, subject, classes=set()):
        self.subject = subject
        self.classes = classes


def printStudents(number):
    for student in classDict[number].students:
        print(student)


while True:
    userTypeName = input().strip()
    if userTypeName == "uczen":
        classNumber = input()
        if classNumber not in classDict:
            classDict[classNumber] = Klasa({input()})
        else:
            classDict[classNumber].students.add(input())
    elif userTypeName == "nauczyciel":
        teacherId = input()
        teacherDict[teacherId] = Nauczyciel(input())
        teacherClasses = input()
        while teacherClasses:
            teacherDict[teacherId].classes.add(teacherClasses)
            if teacherClasses not in classDict:
                classDict[teacherClasses] = Klasa()
            teacherClasses = input()
    elif userTypeName == "wychowawca":
        classNumber = input()
        if classNumber not in classDict:
            classDict[classNumber] = Klasa(hometeacher=input())
        else:
            classDict[classNumber].hometeacher = input()
    elif userTypeName == "koniec":
        break
    else:
        print("Nieprawidłowy typ użytkownia!")
        exit()
if phrase in classDict.keys():
    print("Wychowawca klasy: {}".format(classDict[phrase].hometeacher))
    print("Uczniowie klasy:")
    printStudents(phrase)
elif phrase[-1] == "H":
    for number, classHTeacher in classDict.items():
        if classHTeacher.hometeacher == phrase:
            printStudents(number)
            break
elif phrase[0] == "T":
    print("Wychowawcy:")
    for classNumber in teacherDict[phrase].classes:
        if phrase in classDict[classNumber].hometeacher:
            print(classDict[classNumber].hometeacher)
elif phrase[0] == "S":
    classNumber = ""
    for number, student in classDict.items():
        if phrase in student.students:
            classNumber = number
    for teacherId, teacherData in teacherDict.items():
        if classNumber in teacherData.classes:
            print(
                "Przedmiot: {}, Nauczyciel: {}".format(teacherData.subject, teacherId)
            )
else:
    print("Nie podano argumentu")
