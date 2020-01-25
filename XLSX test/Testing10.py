from xml.dom import minidom
# mytree=minidom.parse('Sample.xml')
data = open('test.xml')
a = minidom.parse(data)
for i in a[0]:
    print(i)