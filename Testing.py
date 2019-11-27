import pandas as pd
D = {
    'Name':["Abhishek","Sanjay","Ravi"],
    'Age':[23,21,23],
    'Roll no':[423,43,23],
    'Marks':{'Science':89,'Maths':78}
} 
D['Marks']['Computer Science']=98
k={'Computer Science':98}
'''for i in D:
    if i == 'Marks':
        D['Marks']=k'''
print(D)