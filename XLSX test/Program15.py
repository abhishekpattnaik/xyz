import pandas as pd 
import xml.etree.ElementTree as ET
tree = ET.parse('test.xml')
root = tree.getroot()
tempDict={}    
dataframe = pd.DataFrame()
for ele in root:
    for sub_ele in ele:
        tempDict[sub_ele.tag]=sub_ele.text
    dataframe=dataframe.append(tempDict,ignore_index=True)
dataframe.to_excel('Test1.xlsx')
print(dataframe)
print('Completed')