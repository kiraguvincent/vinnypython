# Data Types
number = 45  # int
num= 56.78  # float
greeting = "Hello there"  # str
isPythonInteresting=True #bool

# Variable Storing Multiple Values
languages = ["Python", "php", "Java"]  # list
fruits = ("apple", "banana", "pineapple")  # Tupple
Countries = {"Kenya", "China", "USA"}  # set
# Dictionary
details={
    "first_name": "Grace",
    "Age":17,
    "Course":"MIT",
    "Nationality":"North America"
}
print(number)
print(greeting)
print(Countries)
print(isPythonInteresting)
print(details["Course"])
print(details)
print(details["Nationality"])
#Determining the data type
print(type(details))
print(type(Countries))

#Type Casting -Converting one data type to another
print(int(num))
print(float(number))