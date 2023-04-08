from itertools import chain
x=[[1,2,3],[4,5]]
y=[['a','b','c'],['d','e']]
res=list(zip(chain.from_iterable(x),chain.from_iterable(y)))
print(str(res))
