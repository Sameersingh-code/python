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
