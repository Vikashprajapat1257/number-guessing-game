import random

num = random.randint(1,100)
i=0
while(True):
    new = int(input("Enter a number: "))
    i+=1
    if(num == new):
        print("correct")
        break
    elif(num>new):
        print("too low")
    elif(num<new):
            print("too high")

print("In",  i , "Attempts")

