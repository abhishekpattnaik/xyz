import xml.etree.ElementTree as ET
import pandas as pd
tree = ET.parse('XML test/deal1.xml')
root = tree.getroot()
D={}
dataFrame = pd.DataFrame()
for units in root.find('Units'):
    for sub_units in units:
        # print(sub_units.tag,'=',sub_units.text)
        D[sub_units.tag]=sub_units.text
    dataFrame=dataFrame.append([D],ignore_index=True)
# dataFrame.to_excel('XML test/deal1_XML_to_XLSX.xlsx')
print(dataFrame)