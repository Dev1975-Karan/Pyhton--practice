import random as rd#correct

print(" \"Hi!, My self Dev and welcome to the number gussing game.\"\n","\"Rules are simple, you decide the range but we actually decide the number you have to guess(you have 5 chances.).\"\n","\"So,Let's begin it!!!\"")
a=int(input(" Enter your lower bound:" ))#a and b will decide the range for gussing the no.
b=int(input(" Enter your upper bound:"))
c=rd.randint(a,b)
ch=5
gc=0
while(gc<ch):
    gc+=1
    df=ch-gc
    guess=int(input(" Enter your guess no: "))
    if(guess==c):
        print("\"you have gussed the correct number!!\"\n",f"The number is {c}")
        break

    elif(guess>c):
        print("you guessed the large number.")
        print(f"the no. of chances left {df}")
    elif(guess<c):
        print("you gussed the samll no.")
        print(f"the no. of chances left {df}")
if(gc>=ch) and(guess!=c):
  print(f"Sorry! the number was {c}. Better luck next time.")

    
    

     