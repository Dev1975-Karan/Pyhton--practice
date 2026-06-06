#WAP to define the function to provide the factorial of no.
#Solution
def fact(x):
    if x==0:
        return 1
    return x*fact(x-1)
n=int(input("enter your number: "))
print(fact(n))