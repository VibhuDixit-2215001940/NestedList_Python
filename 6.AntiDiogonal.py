#Printing Upper Half Elements
r=int(input("Enter the no. of rows: "))
c=int(input("Enter the no. of columns: "))
x=[]
for i in range(r):
    y=[]
    for i in range(c):
        z=input("Enter value: ")
        y.append(z)
    x.append(y)
for i in range(r):
    for j in range(c):
        if(i+j==r-1):
            print(x[i][j],end=' ')
        else:
            print(" ",end=" ")
    print()