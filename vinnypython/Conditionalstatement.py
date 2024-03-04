Temparature=13
if Temparature>25:
    print("It is hot")
else:
    print("It is cold")


    #a programme that returns the largest number among three numbers
    num1=45
    num2=46
    num3=21
    if num1>num2>num3:
        print(num1, "is the largest number")
    elif num2> num1 and num2 > num3:
        print(num2, "is the largest number")
    else:
       print(num3, "is the largest number")

    #A programme that checks whether a number is even or odd
    number=45
    if number % 2==0:
        print(number,"is even")
    else:
         print(number,"is odd")

    #A programme that checks whether a number is prime or not
    number1=20
    for i in range(2,number1):
        if number%i==0:
            print(number1,"is not a prime number")
            break
        else:
            print(number1,"is a prime number")
