import pandas as pd 

D1 = {
    'Name':['Abhishek','Abhijit','Ravi','Rupak','Sanjay','Sarvottam','Sachin'],
    'ID':[101,102,103,104,105,106,107],
    'Marks':[98,78,89,89,65,45,58],
    'Age':[23,21,22,23,22,25,21]
}
x1 = pd.DataFrame(D1)
D2 = {
    'Name':['Rohit','Satya','Alia'],
    'ID':[108,109,110],
    'Regn no.':[57476,576675,54645]
}

D3 = {
    'ID':[101,102,103],
    'Gender':['m','m','m']
}
x2 = pd.DataFrame(D3)
#x3 = pd.concat([x1,x2],axis=1,join='inner')
x3 = pd.merge(x1,x2,on=['ID'],how='inner')
print(x3)