from random import random


print("Number Guessing Game")
print("Guess the number between 1-5")
random=int(input("Enter a number"))
if(random<=2):
    print("Your guess is close; think of 2 more numbers")
elif(random<=3):
    print("Your guess is little wrong; think of one more greater number")
elif(random==4):
    print("CONGRATULATIONS!!! YOU WON")
