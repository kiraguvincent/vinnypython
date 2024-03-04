class Animal:
     def speak(self):
         print("Animal is speaking")
   #Child class /sub class/Derived class
class Dog(Animal):
    def bark(self):
        print("Dog is barking")

class Cat(Dog):
    def meow(self):
        print("Cat is meowing")

a=Animal()
d=Dog()
d.bark()
d.speak()
c=Cat()
c.meow()
c.speak()
