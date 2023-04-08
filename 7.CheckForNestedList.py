lst=[[1,2,3],[4,5,6],[7,8,9]]
for i in lst:
    if type(i) is list:
        result=True
        break
print("Does the the given list is nested list: "+str(result))