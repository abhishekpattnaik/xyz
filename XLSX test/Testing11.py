import xml.etree.ElementTree as ET
mytree = ET.parse('test.xml')
myroot = mytree.getroot()
# ET.SubElement(myroot[0],'speciality')
for x in myroot[0]:
    print(x)
# mytree.write('new.xml')