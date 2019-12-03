import pandas as pd 
x1 = pd.read_excel('file1.xlsx')
#x1 = x1.rename(columns={'Roll No':'RN'})
x2 = pd.read_csv('cars.csv')
#print(x2)
k=0
c=0
print(x2[["Car’s Name"][0:5]])
#x3 = x1.iloc[0,0]
x3 = x1.loc[x1['Name']=='Abhishek']
#print(x3)