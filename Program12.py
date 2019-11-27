import pandas as pd
x1 = pd.read_excel("trafficking.xlsx")
x1=x1.loc[x1['advertiser_name']=='StockX']
#print(x1.sort_values('brand_name'))
#x3 = pd.merge(x1,x2,on=['ID'],how='inner')
print(x1.show)