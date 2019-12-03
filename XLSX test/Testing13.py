import xml.etree.ElementTree as ETT
# import xml.dom.minidom as ET
from xml.dom import minidom
dat= '''
<persons>
    <person>
        <name>Chuck</name>
        <phone type="intl">
            +91 8480079939
        </phone>
        <email hide = "yes"/>
    </person>
    <person>
        <name>Dannis</name>
        <phone type="intl">
            +91 8480079935
        </phone>
        <email hide = "yes"/>
    </person>   
</persons>
'''
domm = minidom.parse(dat)
items = domm.getElementsByTagName('persons')
for item in items:
    # print(item.attributes['name'].value)
    print(item)
# print(items)