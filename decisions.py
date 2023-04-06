import random

number = random.randint(0,10)

print(number)

if(number > 6): 
    print("Big number")
elif(number < 6): # else if
    print("Small number")
else: # elif(number == 6):
    print("Number is 6")