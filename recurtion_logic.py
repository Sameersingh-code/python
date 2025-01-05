#Recurstion is process of the defining something  the term of itself.
#How to impiliment fibonacci series
#def fibonacci(n):
#     if n==1:
#         return 1
#     elif n==0:
#         return 0
#     else:
#         return fibonacci(n-1) +fibonacci(n-2)
# print(fibonacci(int(input("Enter a number : "))))
# Example input 3 then output 2
def fact(n):
    if(n == 1 or n == 0):
        return 1
    else:
        return n*fact(n-1)
print(fact(int(input("Enter a number : "))))
#Example input 5 then output 120
#how to call one function in another function by using one function
#cheak the number is odd or even
def even_recurstion(x):
    if x == 0:
        return 1
    else:
        return odd_recurstion(x-1)
def odd_recurstion(x):
    return not even_recurstion(x)
print(even_recurstion(10))
print(odd_recurstion(9))
#output Ture , Ture
