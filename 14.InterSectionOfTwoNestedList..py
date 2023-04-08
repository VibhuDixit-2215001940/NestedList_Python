x=[[1,2,3],[4,5],[6,7,8]]
y=[[4,5],[2,6,9]]
res=[]
for i in x:
    if i in y:
        res.append(i)  
print(res)