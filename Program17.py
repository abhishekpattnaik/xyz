import xml.etree.ElementTree as ET
data = ET.Element('data')
items = ET.SubElement(data,'items')
item1 = ET.SubElement(items,'item')
item2 = ET.SubElement(items,'item')
# item1.set('name','item1')
# item2.set('name','item2')
item1.text = 'item1abc'
item2.text = 'item2abc'
mydata = ET.tostring(data)
myfile = open("test1.xml","wb")
myfile.write(mydata)