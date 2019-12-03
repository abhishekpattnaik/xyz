from numpy import *
L = [1,2,3,4,5,6,7,8,9]
evens = list(filter(lambda n : n%2==0,L))
#print(evens)
def div(a,b):
    return a/b
def smart_div(func):
    def inner(a,b):
        if(a<b):
            a,b=b,a
            return func(a,b)
    return inner
div1 = smart_div(div)
print(div1(4,8))