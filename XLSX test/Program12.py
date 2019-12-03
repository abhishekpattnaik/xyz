<<<<<<< HEAD
import pandas as pd 
x1 = pd.read_excel("trafficking.xlsx")
x1=x1.loc[x1['show']=='Forged By the Gods']
#print(x1.sort_values('brand_name'))
#x3 = pd.merge(x1,x2,on=['ID'],how='inner')
=======
import pandas as pd
x1 = pd.read_excel("trafficking.xlsx")
x1=x1.loc[x1['advertiser_name']=='StockX']
#print(x1.sort_values('brand_name'))
#x3 = pd.merge(x1,x2,on=['ID'],how='inner')
print(x1.show)
>>>>>>> 6746aa6d14a395c0321bc86e5e739422241c7dab
