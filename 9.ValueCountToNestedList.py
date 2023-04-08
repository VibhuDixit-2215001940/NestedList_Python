y=list(map(int,input("Enter no.: ").split()))
print(y)
x=[]
for i in range(0,len(y)):
    j=[i+1]
    x.append(j*y[i])
print(x)