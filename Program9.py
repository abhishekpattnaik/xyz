import pandas as pd 
import xml.etree.ElementTree as ET
x1 = pd.read_excel('Sample.xlsx',sheet_name='Sheet1')
root_element = ET.Element('rootName')
sale = ET.SubElement(root_element,'sale')
for count in range(len(x1)):
    person = ET.SubElement(sale,'person')
    for row in x1:
        row = ET.SubElement(person,row)
        for items in row:
            # row.text='xyz'
            print(items)
# mydata = ET.tostring(root_element)
# myfile = open("test1.xml","wb")
# myfile.write(mydata)
# print(len(x1))

print(x1.iloc[0])