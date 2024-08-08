# this modulle help to generate random number
import random

# here we ask computer to take any random number from 0,1, 2

computer=random.randint(0, 2)
# ask the user to give there input 
user=int(input("0 for snake,1 for water, 2 for gun: "))
print(computer)
# function for playing 
def play(computer, user):
    if(computer==user):
        return 0
    elif(computer==1 and user==2):
        return -1
    elif(computer==0 and user==1):
        return -1
    elif(computer==2 and user==0):
        return -1
    else:
        return 1
# give the return value to score 
score= play(computer, user)
if (score==0):
    print("draw")
elif(score==1):
    print("win")
else:
    print("lose")
