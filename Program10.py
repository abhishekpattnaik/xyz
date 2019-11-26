import pandas as pd 
x1 = pd.read_excel(r'file1.xlsx',sheet_name='file1')
D = {}
L = []
for i in x1:
    D[i]=x1[i].tolist()
    L.extend(x1[i].tolist())
x1 = pd.DataFrame(D)
print(x1)