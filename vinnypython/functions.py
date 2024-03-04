# Inbuilt functions
number = max(89, 70, 23, 45, 123)
print(number)

x = min(78, 45, 34, 1, )
print(x)

z = pow(2, 3)
print(z)


# User defined functions
def name():
    print("Vincent")


name()  # Calling a function


def student():
    name = "Vincent"
    Age = 18
    Course = "MIT"
    print(name, Age, Course)


# Parameters/variables and arguments/values
def students(name , Age, course):
    print(name, Age, course)
students("Vincent", 18, "MIT")
students("Jade", 17, "Datascience")
students("Joy", 15, "MIT")
students("Grace", 19, "MIT")
students("Ann", 16, "MIT")
students("Ann", 16, "MIT")
students("Ann", 16, "MIT")

# Create a user-defined function
# called employees.It should display
# details of five employees.Parameters are
# fullname ,age ,gender ,position  ,salary


#User defined function _employees
#Parameters
def employees(fullname,age,gender,position, salary):
             print(fullname, age, gender, position,salary)
employees("Joasn on",25,"Female","CEO",510000)
employees("Pare Wun",23,"Male","Manager",210000)
employees("Glory Tas h",35,"Female","Web developer",1000000)
employees("Jessy Maut",35,"Female","Accountant",610000)
employees("Seanice joy",21,"Female","Lecturer",1080000)
