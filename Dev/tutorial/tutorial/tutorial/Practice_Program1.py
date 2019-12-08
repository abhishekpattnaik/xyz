fibonacci_cache = {}
def fibonacci(num):
    if num in fibonacci_cache:
        return fibonacci_cache[num]
    if num==1:
        value=1
    elif num==2:
        value=1
    elif num > 2:
        value= fibonacci(num-1)+fibonacci(num-2)
    fibonacci_cache[num]=value
    return value
user_input=int(input("PLease enter the range"))
for x in range(1,user_input):
    print(x,":",fibonacci(x))