from datetime import date
import datetime

class Person():

    def __init__(self, name, birthday, city):
        self.name = name
        self.birthday = date.fromisoformat(birthday)
        self.city = city
    
    def introduce_yourself(self):
        print("Hello, my name is", self.name)
       
    def age_person(self):
        now = datetime.datetime.now()
        age = None
        
        if now.month >= self.birthday.month:
            age = str(now.year - self.birthday.year)
        else:
            age = str(now.year - self.birthday.year - 1)
        print ("You are " + age + " y.o")
    
person1 = Person('Eric', '1998-07-11', 'Kyiv')
person1.introduce_yourself()
person1.age_person()

class Student(Person):
    def __init__(self, name, birthday, city, univer, end_of_study, avg_mark):
        super().__init__(name, birthday, city)
        self.univer = univer
        self.end_of_study = end_of_study
        self.avg_mark = avg_mark
    def print_student(self):
        print("\n")
        print("Student name: ", self.name)
        print("Date of birth", self.birthday)
        print("Place of birth", self.city)
        print("This student study at", self.univer)
        print("This student will graduated in", self.end_of_study)
        print("Now this student have such an averange mark", self.avg_mark)

def display_message1():
	return "All about Python!"

student1 = Student('Jordan', '1999-08-20', 'Sumy', 'Sumy State University', 2023, 91.7)
student1.print_student()
student2 = Student('Mike', '1999-03-16', 'Lviv', 'Lviv National University', 2024, 65.3)
student2.print_student()
student3 = Student('Vadim', '1998-12-16', 'Kharkiv', 'Kharkiv National University', 2022, 80.1)
student3.print_student()    
