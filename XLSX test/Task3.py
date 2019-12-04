import pandas as pd
def searchQuery(dataFrame,inputSearch):
    if dataFrame['Advertiser_name'].str.contains(inputSearch).any():
        return dataFrame.loc[dataFrame['Advertiser_name']==inputSearch]
    elif dataFrame['Brand_name'].str.contains(inputSearch).any():
        return dataFrame.loc[dataFrame['Brand_name']==inputSearch]
    elif dataFrame['Shows'].str.contains(inputSearch).any():
        return dataFrame.loc[dataFrame['Shows']==inputSearch]
    else: return 'Input query not found'
dataObj = pd.read_excel('XLSX test/trafficking.xlsx')
dataObj = pd.DataFrame({'Advertiser_name':dataObj['advertiser_name'],'Brand_name':dataObj['brand_name'],'Shows':dataObj['show']})
print(searchQuery(dataObj,input('Enter the input')))