import pandas as pd 
<<<<<<< HEAD
x1 = pd.read_excel(r'file1.xlsx',sheet_name='file1')
=======
x1 = pd.read_excel(r'trafficking.xlsx')
>>>>>>> 6746aa6d14a395c0321bc86e5e739422241c7dab
D = {}
L = []
for i in x1:
    D[i]=x1[i].tolist()
    L.extend(x1[i].tolist())
x1 = pd.DataFrame(D)
print(x1)