class STUDENT:
    def __init__(self):
        self.usn = None
        self.name= None
        self.age=0
    def getdata(self): 
        try:
            self.usn=str(input("enter student usn number :"))
            self.name=str(input("enter student name :"))
            self.age=int(input("enter student age :"))
        except :
            print("enter valid input")
class STUDCAL(STUDENT):
    def __init__(self):
        self.subject1=0
        self.subject2=0
        self.subject3=0
        self.subject4=0
        self.subject5=0
    def get_and_calculate(self):
        try:
            self.subject1=int(input("enter subject 1 marks :"))
            self.subject2=int(input("enter subject 2 marks :"))
            self.subject3=int(input("enter subject 3 marks :"))
            self.subject4=int(input("enter subject 4 marks :"))
            self.subject5=int(input("enter subject 5 marks :"))
        except:
            print("enter valid input")
        finally:
            if(self.subject1<40 or self.subject2<40 or self.subject3<40 or self.subject4<40 or self.subject5<40):
                self.flag=0
            else:
                self.flag=1
                self.total_marks=self.subject1+self.subject2+self.subject3+self.subject4+self.subject5
                self.percentage=(self.total_marks/500)*100
class STUDDIS(STUDCAL):
       def display_student(self):
        if(self.flag==1):
             print(f"student name :{self.name}\nstudent usn :{self.usn}\nstudent age :{self.age}\nstudent total marks : {self.total_marks} out of 500\nstudent percentage :{self.percentage}\n" )
        else: 
            print(f"{self.name} falid in one of subjects")
while True:
 sn=STUDDIS()
 sn.getdata()
 sn.get_and_calculate()
 sn.display_student()
