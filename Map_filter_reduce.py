#How to impliment map, filter & reduce

# def double(x):
#     return x*x
    
# print(double(2))
# def cube(x):
#     return x*x*x
# l = [1,2,4,8,16]
# AddList = []
# for item in l:
#     AddList.append(cube(item))
# print(AddList)
#map
l = [2,3,4,5]
Mlist = list(map(lambda x: x*x, l))
print(Mlist)
#filter
l = [ 4,5,7,8]
Flist = list(filter(lambda x: x>5, l))
print(Flist)
from functools import reduce
#reduce 
l = [5,6,8,2]
Rlist = reduce(lambda x,y: x+y, l)
print(Rlist)

