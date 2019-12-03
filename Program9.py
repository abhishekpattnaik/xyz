import pandas as pd 
import xml.etree.ElementTree as ET
x1 = pd.read_excel('Sample.xlsx',sheet_name='Sheet1')
root_element = ET.Element('rootName')
sale = ET.SubElement(root_element,'sale')
for row in x1:
    print(row)
# print(x1)