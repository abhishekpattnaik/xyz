import pandas as pd 
import pprint 
x1 = pd.read_excel('trafficking.xlsx')
c = 0
D = {}
for i in x1.advertiser_name:
    x2=x1.loc[c]
    c=c+1
    if i in D.keys():
        if x2.brand_name in D[i].keys():
            D[i][x2.brand_name].append(x2.show)
        else:
            D[i][x2.brand_name]=[x2.show]
    else:
        D[i]={x2.brand_name:[x2.show]}
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(D)