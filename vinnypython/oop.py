class Person:
    def __init__(self,firstname,age,gender):
        self.firstname=firstname
        self.age = age
        self.gender=gender
        def details(self):
            print(self.firstname,"is studying")

teacher=Person("Joe",30,"male")
accountant=Person("John",38,"male")
doctor=Person("Joy",32,"female")
manager=Person("mary",60,"female")

print(teacher.firstname,teacher.age,teacher.gender)
print(accountant.firstname,accountant.age,accountant.gender)
print(doctor.firstname,doctor.age,doctor.gender)
print(manager.firstname,manager.age,manager.gender)
