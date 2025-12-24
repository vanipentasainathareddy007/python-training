#1.fizzbuzz
x=int(input())
for i in range (1,x+1):
    if((i%3==0)&(i%5==0)):
        print('fizz buzzz')
    elif(i%3==0):
        print('fizz')
    elif(i%5==0):
        print('buzz')
    else:
        print(i)
#2.pattern printing.
#a.square
x=int(input())
for  i in range(x):
    for j in range(x):
        print("*",end=" ")
    print("\n")
#b.right angled
x=int(input())
for  i in range(x):
    for j in range(i+1):
        print("*",end=" ")
    print()
#c.right angled in numbers
x=int(input())
for  i in range(x):
    for j in range(i+1):
        print(j+1,end=" ")
    print()
#d.pyramid
x=int(input())
for  i in range(x):
    for j in range(x-i-1):
        print(" ",end=" ")
    for j in range(i+1):
        print("*  ",end=" ")
    print("\n")
#4.diamond
x=int(input())
for  i in range(x):
    for j in range(x-i-1):
        print(" ",end=" ")
    for j in range(i+1):
        print("*  ",end=" ")
    print("\n")
for  i in range(x-2,-1,-1):
    for j in range(x-i-1):
        print(" ",end=" ")
    for j in range(i+1):
        print("*  ",end=" ")
    print("\n")
#5.odd sequence
x=int(input())
for  i in range(x+4):
    for j in range(x-i+4):
        print(" ",end=" ")
    for j in range(i+1):
         if(i%2!=0):
            break
         else:
            print("*  ",end=" ")
    print()

#6.hollow square
n=int(input())
for i in range (n):
    for j in range (n):
        if i==0 or j==0 or i==n-1 or j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
#hollow right angle pyramid
n=int(input())
for i in range (n):
    for j in range (i+1):
        if i==n-1 or j==0 or i==j :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    

        

