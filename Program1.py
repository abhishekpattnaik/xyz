L = [{"name":"Abhishek","Id":101},
    {"name":"Arshad","Id":102},
    {"name":"Sachin","Id":103}]
#print(L)
op=[]

for y in L:
    op.append({y["name"]:y["Id"]})
for x in op:
    for y in x.values():
        print(y)
print(op)