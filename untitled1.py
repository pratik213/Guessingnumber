import random
a=int(input("Enter a number you have guessed from 1-20  :s"))
b=random.uniform(1,21)
if(a>b):
    print("Your guessed number is high ")
elif(a<b):
    print("Your guessed number is less")
else:
    print("You have guessed it correct")