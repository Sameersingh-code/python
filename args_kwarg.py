def tsum(*args):
    return sum(args)
print(tsum(1,2,3,4))
def decarg(**args):
    return args
print(decarg(a=1, b =3, c =5))
#How to find minimum number in list
def lmin(a,b,*args):
    minimum = min(a,b,*args)
    return minimum
    
print(lmin(12,14,15,3,5,6))
