import pandas as pd 
import xml.etree.ElementTree as ET
tree = ET.parse('test.xml')
root = tree.getroot()
# D=root[0][0].attrib
# print(D.keys)
# for ele in root:
#     for subele in ele:
#         print(subele.attrib)
# print(root[0][1].text)
# for ele in root:
#     for sub_ele in ele:
#         print(ele[0].attrib,sub_ele.text)
# for ele in root[0]:
#     print(ele.text)
# print(root[0].text)
# for ele in root:
#     print(ele[0].text)
# print(root.getchildren.text)
# for elem in root:
#     for subelem in elem:
#         # for x in subelem.keys():
#         #     print(x)
#         print(subelem.items())
# for ele in root:
#     for subele in ele:
#         print(subele.text)
# for ele in root:
#     print(ele.text)
D={}    
L=[]
for ele in root:
    for sub_ele in ele:
        D[sub_ele.tag]=sub_ele.text
        L.extend(D)
dataframe=pd.DataFrame(L)
dataframe.to_excel('Test1.xlsx')
print('Completed')