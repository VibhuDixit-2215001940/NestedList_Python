#Taking Input From User And Printing Two Ways
r=int(input("Enter the no. of rows: "))
c=int(input("Enter the no. of columns: "))
x=[]
for i in range(r):
    y=[]
    for i in range(c):
        z=input("Enter value: ")
        y.append(z)
    x.append(y)
print(x)            #Sequential Printing
for i in range(r):
    for j in range(c):
        print(x[i][j],end=' ')
    print()