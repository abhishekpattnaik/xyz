import xml.etree.ElementTree as ET
mytree = ET.parse('Sample.xml')
myroot = mytree.getroot()
ET.SubElement(myroot[0],'speciality')
for x in myroot.iter('speciality'):
    x.text=str('South Indian Special')
mytree.write('new.xml')