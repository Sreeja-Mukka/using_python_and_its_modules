import random

fruits={'apple':['Is one of the most common fruits consumed all around the world','It is a dietary fibre and has Vitamin C content','Usually red and green in colour'],
'banana':['It is yellow in color and very sweet','is very soft and does not have any hard substance','helps you to gain weight'],
'mango':['Is the national fruit of India','Is the king of fruits','Summer is the season when Indians wait for this fruit']}
animals={'dog':['a domestic animal','They have four legs and one tail','They are playful, friendly and loyal to humans'],
'cat':['one of the popular pet animals','they produce a “meow”, “purr” and “hiss” sound',' is a carnivore animal'],
'monkey':['they love bananas','is found in all forests and zoos','is very naughty animal']}
colors={'red':['one of the three primary colors, along with blue and yellow','is a color of blood','its light has a wavelength between 630-740 nanometers'],
'green':['Color of nature','most restful and relaxing color for the human eye to view','is often used to indicate safety'],
'blue':['a color used to show coldness',' is the color of the Earths sky and sea','popular color for jeans pants']}

def index(ch,inp):
    return [i for i, ltr in enumerate(ch) if ltr == inp]
    
def check(n,k):
    print('The category we choosed is:',n)
    l=random.choice(list(k.keys()))
    length=len(l)
    print("The Length of the word is:",length)
    return l
    
def doit(ind,inp,ch,res):
    print(res)
    r=''
    for i in (ind):
        print(i,"lol")
        res[i]=inp
    r="".join(res)
    print(r)
    if r==ch:
        print('Kudos!')
        return 0
    else:
        for i in res:
            print(i,end=' ')
        return res
    
def guessit(ch):
    d={0:'H',1:'A',2:'N',3:'G',4:'M',5:'A',6:'N'}
    f,c,p=0,0,0
    st=''
    s=''
    flag=0
    r=['-'for i in range(len(ch))]
    print(r)
    while(f<7):
        if flag==1:
            break
        print("enter a character")
        inp=input()
        if inp in ch:
            l=index(ch,inp)
            print(l)
            res=doit(l,inp,ch,r)
            if res==0:
                flag=1
            r=res
        else:
            if c>3:
                print("oops no more hints")
            else:    
                print("noo look at the hint")
                print(k[ch][c])
                c+=1
            s+=d[p]
            p+=1
            f+=1
            print("Your hangman state is:",s)
    if flag!=1:
        print("oops, the word is:",ch)

print("This is HANGMAN! Do you know what hangman is?")
print("Here how it works!")
print("Rule no 1. you need to guess a the word ")
print("Rule no 2. you will get to know what category is choosen, for example it could belong to animals,fruits,colors")
print("Rule no 3.You will need to guess the word before the hangman fills")
print("You should enter single character at a time ex:a , b not ab or ba")
print("You get only 3 hints and these hints will be shown when you enter a wrong character")
print("You will know the length of the word.")
print("Easy rules right? lets do it!")
print("if ready say yes")

cat=[fruits,animals,colors]
op=['fruits','animals','colors']
ki=input()

while(ki=='yes'):
    k=random.choice(cat)
    r=cat.index(k)
    ch=check(op[r],k)
    guessit(ch)
    print("Wanna continue?")
    ki=input()
print("Thank you for playing")