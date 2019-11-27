import pandas as pd 
x1 = pd.read_excel(r'trafficking.xlsx')
D = {}
L = []
for i in x1:
    D[i]=x1[i].tolist()
    L.extend(x1[i].tolist())
x1 = pd.DataFrame(D)
print(x1)