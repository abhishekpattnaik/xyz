import pandas as pd 
x1 = pd.read_excel('trafficking.xlsx')
c = 0
D = {}
for i in x1.advertiser_name:
    x2=x1.loc[c]
    c=c+1
    if i in D.keys():
        D[i][x1.brand_name].append()
        print('...')
    else:
        D[i]={x2.brand_name:[x2.show]}
x3 = pd.DataFrame(D)
x3.to_csv('testing1.csv')
# print(D.values())
# D[i][x2.brand_name]=D[i][x2.brand_name].append([x2.show])