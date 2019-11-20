L = [{"name" : "Abhishek", "id" : 11},{"name" : "Udipta", "id" : 27},{"name" : "Arti", "id" : 21}] 
ll=[]
min = L[0]["id"]
for i in range(len(L)): 
    ll.append({L[i]["name"]:L[i]["id"]})
for k in ll:
    for name, id in k.items():
        if(id<min):
            min = id
for k in ll:
    for name, id in k.items():
        if(id==min):
            print(k)