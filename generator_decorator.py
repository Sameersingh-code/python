#How to impliment decorator in python 
''' Decorator is use for concatenate two function by call one fuction That's mean we can pass another  fuction in middle of funtion.'''
def deco(fn):
    def mfn():
        print("Hey")
        fn()
        print("How are You")
    return mfn
@deco
def first_name():
    print("Sameer")
first_name()
    
# def deco(fn):
#     def mfn(name):
#         print("Hey")
#         fn(name)
#         print("How are You")
#     return mfn
# @deco
# def first_name(name):
#     print(" "+ name)
    
# first_name(input("Enter your name : \n"))

#How to impiliment Genrator
# def genrator():
#     for i in range(10):
#         yield i

# new = genrator()
# print(next(new))
# print(next(new))
# print(next(new))
# for i in new:
#     print(i)

def genrator():
    for i in range(1 , 10):
        yield(i)
        

print(list(genrator()))
