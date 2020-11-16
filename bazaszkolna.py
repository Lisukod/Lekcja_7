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


while True:
    userType = input()
    if userType == "uczen":
        classNumber = input()
        if classNumber not in classDict:
            classDict[classNumber] = Klasa({input()})
        else:
            classDict[classNumber].students.add(input())
    elif userType == "nauczyciel":
        teacherName = input()
        teacherDict[teacherName] = Nauczyciel(input())
        teacherClasses = input()
        while teacherClasses:
            teacherDict[teacherName].classes.add(teacherClasses)
            teacherClasses = input()
    elif userType == "wychowawca":
        classNumber = input()
        if classNumber not in classDict:
            classDict[classNumber] = Klasa(hometeacher=input())
        else:
            classDict[classNumber].hometeacher = input()
    elif userType == "koniec":
        break
    else:
        print("Nieprawidłowy typ użytkownia!")
        exit()
if phrase in classDict:
    print("Wychowawca klasy: {}".format(classDict[phrase].hometeacher))
    print("Uczniowie klasy:")
    for student in classDict[phrase].students:
        print(student)
