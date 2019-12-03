#transfer data from xlsx to xml
import pandas as pd 
import xml.etree.ElementTree as ET
x1 = pd.read_excel('AMN.xlsx')
root_element = ET.Element('rootName')
sale = ET.SubElement(root_element,'sale')
for count in range(len(x1)):
    person = ET.SubElement(sale,'person')
    temp_row = x1.iloc[count]
    for row in x1:
        strig_temp = str(temp_row[row])
        row = ET.SubElement(person,row)
        row.text = strig_temp
mydata = ET.tostring(root_element)
myfile = open("test1.xml","wb")
myfile.write(mydata)