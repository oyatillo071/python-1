class Person:
    def __init__(self,name,surname):
        self.name=name
        self.surname=surname
    def output_data(self):
        return f"Assalom aleykum {self.surname,self.name}"
class Job(Person):
    def __init__(self,name,surname,job):
        super().__init__(name,surname)
        self.job=job
    def greeting(self):
        return f"Assalom aleykum men {self.surname} {self.name} va mening kasbim {job}"
        

name=input("Ismingiz")
surname=input("Familiya ")
job=input("Kasbingiz")
user_data=Person(name,surname)
student_data=Job(name,surname,job)
print(user_data.output_data())
print(student_data.greeting())


