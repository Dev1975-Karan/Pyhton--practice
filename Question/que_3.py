""" Question:
With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary. """

#Solution:

#creating a empty dictionary(say d):
d=dict()
#taking user input:
num=int(input("enter the number: "))
#using for loop:
for i in range(1,num+1):
 d[i]=i**2 #sqaure of i
print(d)