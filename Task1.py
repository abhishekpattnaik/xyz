import pandas as pd 
x1 = pd.read_excel('trafficking.xlsx')
c = 0
D = {}
for i in x1.advertiser_name:
    x2=x1.loc[c]
    c=c+1
    D[i]={x2.brand_name:[x2.show]}
x3 = pd.DataFrame(D)
x3.to_csv('testing1.csv')