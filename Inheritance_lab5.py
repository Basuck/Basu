class Student:
    def _init_(self):
        self.usn = None
        self.name = None
        self.age = None

    def get_data(self):
        self.usn = input("Enter usn of student: ")
        self.name = input("Enter name of student: ")
        self.age = input("Enter age of student: ")

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("USN:", self.usn)

class PGStudent(Student):
    def _init_(self):
        super()._init_()
        self.sem = None
        self.fees = None
        self.stipend = None

    def pg_get_data(self):
        super().get_data()
        self.sem = input("Enter semester of student: ")
        self.fees = input("Enter fees of student: ")
        self.stipend = input("Enter stipend of student: ")

    def pg_display(self):
        super().display()
        print("Sem:", self.sem)
        print("Fees:", self.fees)
        print("Stipend:", self.stipend)

class UGStudent(Student):
    def _init_(self):
        super()._init_()
        self.sem = None
        self.fees = None
        self.stipend = None

    def ug_get_data(self):
        super().get_data()
        self.sem = input("Enter semester of student: ")
        self.fees = input("Enter fees of student: ")
        self.stipend = input("Enter stipend of student: ")
    
    def ug_display(self):
        super().display()
        print("Sem:", self.sem)
        print("Fees:", self.fees)
        print("Stipend:", self.stipend)

pg = PGStudent()
ug = UGStudent()

print("PG")
pg.pg_get_data()
pg.pg_display()

print("UG")
ug.ug_get_data()
ug.ug_display()
