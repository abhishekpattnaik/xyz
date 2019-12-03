import pandas as pd
column_name = ['Advertiser_Name','Brand_Name','Shows']
dataObj = pd.read_excel('trafficking.xlsx')
# dataObj = pd.DataFrame({'Advertiser_name':dataObj['advertiser_name'],'Brand_name':dataObj['brand_name'],'Shows':dataObj['show']})
dataObj.filter(items=['advertiser_name', 'brand_name','show'])
dataObj.sort_values("advertiser_name", inplace=True)  
dataObj.drop_duplicates(inplace=True)
dataObj.to_excel('AMN.xlsx',index=False)
print(dataObj)