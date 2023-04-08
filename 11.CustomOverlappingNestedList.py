lst=[1,2,3,4,5,6,7,8,9,10,11,12]
step=int(input("Enter the step: "))
size=int(input("Enter the size: "))
res=[]
for i in range(0,len(lst),step):
    res.append(lst[i:i+size])
print(res)
    