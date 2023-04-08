def check(x,y):
    return all(i in x for i in y)
    
lst=[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
mst=[[4,5,6],[7,8,9]]
print(check(lst,mst))