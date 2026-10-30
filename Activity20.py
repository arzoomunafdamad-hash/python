class student:
    grade = 9
    print("Hi i am student of grade", grade)

ob = student()

class student:
    grade = 9
    name = "Arzoo"

    def introduction(self):
        print("Hi I am a student")
    def details(self):
        print("My name is", self.name)
        print("I study in grade", self.grade)

ob = student()
ob.introduction()
ob.details()