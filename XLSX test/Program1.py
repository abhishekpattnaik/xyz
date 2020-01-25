<<<<<<< HEAD
for i in range(int(input())):
    print(i)
=======

L = [{"name":"Abhishek","Id":101},
    {"name":"Arshad","Id":102},
    {"name":"Sachin","Id":103}]
op=[]
for y in L:
    op.append({y["name"]:y["Id"]})
for x in op:
    for y in x.values():
        print(y)
print(op)
>>>>>>> 6746aa6d14a395c0321bc86e5e739422241c7dab
