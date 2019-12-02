import xml.etree.ElementTree as ET
mytree = ET.parse('Sample.xml')
myroot = mytree.getroot()
# for x in myroot.findall('food'):print(x.find('item').text,x.find('price').text)
for x in myroot.iter('description'):
    # a = str(x.text)+