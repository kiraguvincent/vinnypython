#While Loop1
number=5
while number<=10:
    print(number)
    number+=1


#Decrement
num=105
while num>=100:
    print(num)
    num-=1

#Break statement
x=20
while x<=25:
    print(x)
    if x ==24:
        break
    x+=1

    #Continue statement
y=79
while y<85:
        y+=1
        if y==83:
            continue
        print(y)

    #For loop
languages=['Python','Java','c++']
for z in languages:
        print(z)

    #Range
for mynumber in range(5):
    print(mynumber)

for mynum in range(2,6):
    print(mynum)

for count in range(20,30,2):
    print(count)