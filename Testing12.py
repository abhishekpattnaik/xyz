import xml.etree.ElementTree as ET
tree = ET.parse('test.xml')
root = tree.getroot()
print('Expertise Data')
D = {}
for elem in root:
    for subelem in elem:
        # print(subelem.text)
        # pass
        D[elem.text]=subelem.text 
    # print(elem.text)
print(D)