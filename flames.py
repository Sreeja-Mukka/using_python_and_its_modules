'''

                            Online Python Debugger.
                Code, Run and Debug Python program online.
Write your code in this editor and press "Debug" button to debug program.

'''
fi={'F':'Friendship',
    'L':'Love',
    'A':'Affection',
    'M':'Marriage',
    'E':'Enemies',
    'S':'Sister'}
def calculate(k):
    length=6
    ind=0
    l=['F','L','A','M','E','S']
    while(len(l)!=1):
        for i in range(ind,ind+k):
            ind=i%length
        l.pop(ind)
        length=length-1
    return l[0]  
def flames(b,g):
    l1=list(b)
    l2=list(g)
    c,count=0,0
    for i in l1:
        if i in l2:
            d=l2.index(i)
            l2.pop(d)
        else:
            c+=1
    count=c+len(l2)  
    return count
    

def cal(b,g):
    if len(b)>len(g):
        k=flames(g,b)
    else:
        k=flames(b,g)
    p=calculate(k)
    print(fi[p])
    

print("lets recall your childhood and lets starting doing our fav FLAMES")
print("type 'y' to start")
kill=input()
while(kill=='y'):
    print("Enter your name")
    b=input()
    print("Enter your crush name")
    g=input()
    print("so, your relationship status is.....")
    cal(b,g)
    print("press 'y' to start again")
    kill=input()
print("Thank you for playing :)")    