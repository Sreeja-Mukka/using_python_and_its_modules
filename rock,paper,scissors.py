import random
def findthewinner():
    i=0
    l=['rock','paper','scissors']
    computer,user=0,0
    while(i!=5):
        k=random.choice(l)
        print("Enter your choice")
        inp=input()
        if inp in l:
            print("Computer choice",k)
            if k==l[0] and inp==l[2]:
                computer+=1
            elif inp==l[0] and k==l[2]:
                user+=1
            elif k==l[1] and inp==l[0]:
                computer+=1
            elif inp==l[1] and k==l[0]:
                user+=1
            elif k==l[2] and inp==l[1]:
                computer+=1
            elif inp==l[2] and k==l[1]:
                user+=1
        else:
            print("Wrong input!! type only rock/paper/scissors")
        i+=1
    if computer>user:
        print("Oops computer wins",computer)
    elif user>computer:
        print("Wohhoo you win",user)
    else:
        print("ohh its a tie")
        print("Wanna try again??")

print("Lets play Rock, Paper, Scissors")
print("Rules are Simple and easy ")
print("first mov is given by the user and other move is given by our computer")
print("totally there are 5 rounds , the one who gets more score wins!")
print("you need to type only rock,paper,scissors")
print("Ready?")
print("yes/no")
l=input()
while(l=='yes'):
    findthewinner()
    print("Would you like to play again?")
    print("yes/no")
    l=input()
print("Thanks for playing!, see you soon")
    
    
    
    