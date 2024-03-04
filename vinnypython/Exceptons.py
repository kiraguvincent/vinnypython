try:
    print(x)
except:
    print("NameError occurred")

    num1=20
    num2=0
try:
    print(num1/num2)
except:
    print("ZeroDivisionError occurred")





# User-defined function
try:
    def multiply(x,y):
        return x*y
except:
      print("Exception occurred")
finally:
        print("success")

print(multiply(10,20))