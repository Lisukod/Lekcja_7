from sys import argv


class Klasa:
    def __init__(self, number):
        self.number = number


class Uczen:
    def __init__(self, student_id, classroom):
        self.student_id = student_id
        self.classroom = classroom


class Nauczyciel:
    def __init__(self, teacher_id, subject, classrooms=set()):
        self.teacher_id = teacher_id
        self.subject = subject
        self.classrooms = classrooms


class Wychowawca:
    def __init__(self, homeroom):
        self.homeroom = homeroom
