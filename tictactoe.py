def printboard(dict1):
    print("|",dict1[7],"|",dict1[8],"|",dict1[9],"|")
    print("------------")
    print("|",dict1[4],"|",dict1[5],"|",dict1[6],"|")
    print("------------")
    print("|",dict1[1],"|",dict1[2],"|",dict1[3],"|")
    
print("THE TIC TAC TOE")
print("Hi, Welcome to the game , the game rules are simple and most of you know it")
print("Each player gets a chance one by one to play ")
print("lets see who wins?😀")

def check(d):
    if d[1]==d[2]==d[3]:
        return True
    elif d[4]==d[5]==d[6]:
        return True
    elif d[1]==d[2]==d[3]:
        return True
    elif d[7]==d[4]==d[1]:
        return True
    elif d[8]==d[5]==d[2]:
        return True
    elif d[9]==d[6]==d[3]:
        return True
    elif d[7]==d[5]==d[3]:
        return True
    elif d[9]==d[5]==d[1]:
        return True
    else:
        return False

def startgame():
    dict1={1:" ",2:" ",3:" ",4:" ",5:" ",6:" ",7:" ",8:" ",9:" "}
    printboard(dict1)
    f,f1,k=0,0,0
    while(k!=10):
        if(k%2==0):
            print("X it's you're turn")
            print("In which place do you want to place X")
            l=int(input())
            if l in dict1 and dict1[l]==" ":
                dict1[l]='X'
                k+=1
            else:
                print("Select the correct index")
            printboard(dict1)   
            if k>=5:
                flag=check(dict1)
                if flag==True:
                    f1=1
                    break
        else:
            print("O it's you're turn")
            print("In which place do you want to place O")
            l=int(input())
            if l in dict1 and dict1[l]==" ":
                dict1[l]="O"
                k+=1
            else:
                print("Select the correct index")
            printboard(dict1) 
            if k>=5:
                flag=check(dict1)
                if flag==True:
                    f=1
                    break
    if f==1:
        print("O won the match")
    elif f1==1:
        print("X won the match")
    else:
        print("its a tie ")
        
print("This is the intial board the numbers of the indexs are like this ...")
print("7 8 9") 
print("4 5 6")
print("1 2 3")
print("Ready?")
st=input()

while(st=="yes"):
    startgame()
    print("do you want to continue??")
    st=input()
print("Thank You For playing")    