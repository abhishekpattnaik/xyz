import pandas as pd
import xml.etree.ElementTree as ET
def to_dataFrame(root):
    dataframe=pd.DataFrame()
    for ele in root:
        for sub_ele in ele:
            tempDict[sub_ele.tag]=sub_ele.text
        dataframe=dataframe.append(tempDict,ignore_index=True)
    return dataframe
tree = ET.parse('XML test/log1.xml')
root = tree.getroot()
tempDict={}
dataframe = to_dataFrame(root)
# dataframe.to_excel('XML test/Test.xlsx',sheet_name=root[0].tag)
print(dataframe)
print('Completed')