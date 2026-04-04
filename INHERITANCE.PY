class animal:
    def legs(self):
        print("i have a 6 legs")
class dog(animal):
    def legs(self):
        super().legs()
        print("dog have a 4 legs") ## OVERRIDING##
d = dog()
d.legs()

class human:
    def __init__(self,number_of_legs):
        self.number_of_legs = number_of_legs
        self.number_of_hands = 2
        self.num_eyes = 2
class male(human):
    def __init__(self,name):
        super().__init__(2)
        self.name = name
    def display(self):
        print(f"{self.name} has {self.num_eyes} eyes and {self.number_of_legs} legs and {self.number_of_hands} hands")
m1 = male("chetan")
print(m1.display())
print(m1.name)
print(m1.number_of_legs)
print(m1.number_of_hands)
print(m1.num_eyes)

class fruits:
    def __init__(self,name,color):
        self.name =  name
        self.color = color
        self.quality = "good"
    def eatby(self):
        print("mango is eaten by human")
class mango(fruits):
    def eatby(self):
        super().eatby()
        print("mango is eaten by all peopels")
mang = mango("mango","yellow")
print(mang.name)
print(mang.eatby())
print(mang.color)
print(mang.quality)

## MULTIPLE INHERITANCE##

class father:
    def f_skills(self):
        print("software developer", 'and' "programmer")
class mother:
    def m_skills(self):
        print("cooking", "home maker")
class child(father,mother):
    def skills(self):
        self.m_skills ()
        self.f_skills()       
c = child()
c.skills() # MRO(method revolution order) ##

class splendor:
    def __init__(self,brand,model):

        self.brand = brand
        self.model = model
class shine:
    def __init__(self):

        pass

class honda(splendor,shine):
    def __init__(self):
        super().__init__("HF-DELUXC","BF6")
    def display(self):
        print(f"the bike name:{self.brand} and model name:{self.model}")
h1 = honda()
h1.display()

## MULTILEVEL INHERITANCE ## BOTH INIT AND NORMAL METHOD  MRO  ##
class human:
    def eat(self):
        print("i will eat meat")
class female(human):
    def walk(self):
        print("i can't walk properly")
class girl(female):
    def walk(self):
        female.walk(self)
        super().walk()
        print(" i can  walk")
g = girl()
(g.eat())
g.walk()

class HUMAN:
    def __init__(self,eyes):
        self.eyes = eyes
class male(HUMAN):
    def __init__(self,eyes,name,character):
        self.name  = name
        self.character = character
        self.eyes = eyes 
class boy(male):
    def __init__(self,eyes,name,character,hearts,legs,hands):
        self.name = name
        self.hearts = hearts
        self.hand = hands 
        self.eyes = eyes
        self.legs = legs
        self.character = character
         
    def display(self):
        print(f"the details of{self.name}, heart:{self.hearts}, hands:{self.hand}, legs:{self.legs} , eyes:{self.eyes} , character:{self.character}")
b = boy("chetan",1,2,2,2,"good")
##print(b.eyes)
#print(b.name)
b.display()
print(boy.mro())

## HIRARCIAL INHERITANCE##
class university:
    def __init__(self,U_name):
        self.uniname = U_name
class student(university):
    def __init__(self, name):
        super().__init__(U_name = "vtu")
        self.name = name
    def show(self):
        print("------ STUDENT DETAILS -----")
        print(f"university name:{self.uniname},student name:{self.name}")
class faculty(university):
    def __init__(self, U_name,f_name):

        super().__init__(U_name = "VTU")
        self.fname = f_name
    def display(self):
        print("------ FACULTY DETAILS -----")
        print(f"university name:{self.uniname}  faculty is:{self.fname}")
f1 = faculty( "VTU","pavitra")
f1.display()
s1 = student("chetan")
s1.show()

## HYBRID INHERITANCE ##Q

class university:
    def universitya(self):
        print("VTU")
class course(university):
    def coourse(self):
        print("ENGINEERING")
class branch(university):
    def branch1(self):
        print("CSE")
class student(branch,course,university):
    pass
s1 = student()
s1.branch1()
s1.coourse()
s1.universitya()

class university:
    def __init__(self,uname):
        self.uname = uname
class course(university):
    def __init__(self,uname ,cname):
        university.__init__(self,uname )
        self.cname = cname
        
class branch(university):
    def __init__(self,uname,bname):
        university.__init__(self,uname)
        self.bname = bname
class student(course,branch):
    def __init__(self,uname,cname,bname,sname):
        course.__init__(self,uname,cname)
        branch.__init__(self,uname,bname)
        self.sname = sname
    
    def display(self):
        print(f"{self.uname},course name:{self.cname},branch name:{self.bname},student name:{self.sname}")

s1 = student("VTU","CSE","BE","CHETAN")
s1.display()


# Base class
class University:
    def __init__(self, university_name):
        self.university_name = university_name


# Single inheritance
class Branch(University):
    def __init__(self, university_name, branch_name):
        University.__init__(self, university_name)
        self.branch_name = branch_name


# Single inheritance
class Course(University):
    def __init__(self, university_name, course_name):
        University.__init__(self, university_name)
        self.course_name = course_name


# Multiple + Hybrid inheritance
class Student(Branch, Course):
    def __init__(self, university_name, branch_name, course_name, student_name):
        Branch.__init__(self, university_name, branch_name)
        Course.__init__(self, university_name, course_name)
        self.student_name = student_name

    def display_student(self):
        print("Student Name :", self.student_name)
        print("University   :", self.university_name)
        print("Branch       :", self.branch_name)
        print("Course       :", self.course_name)


# Hierarchical inheritance
class Faculty(Branch):
    def __init__(self, university_name, branch_name, faculty_name):
        Branch.__init__(self, university_name, branch_name)
        self.faculty_name = faculty_name

    def display_faculty(self):
        print("Faculty Name :", self.faculty_name)
        print("University   :", self.university_name)
        print("Branch       :", self.branch_name)


# ------------------ Testing ------------------

print("---- Student Details ----")
s = Student(
    "VTU Belagavi",
    "Computer Science",
    "Python Programming",
    "Chetu Ambi")

s.display_student()

print("\n---- Faculty Details ----")
f = Faculty(
    "VTU Belagavi",
    "Computer Science",
    "PROF.SNEHA"
)
f.display_faculty()
