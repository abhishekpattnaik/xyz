import xml.etree.ElementTree as ET
data = ''' <?xml version="1.0" encoding="UTF-8"?>
<metaData>
	<food>
		<item name="Breakfast">Idly</item>
		<price>$2.5</price>
		<description>Two idly's with chutney</description>
		<calories>553</calories>
	</food>
    </metaData>'''
myroot = ET.fromstring(data)
print(myroot.tag)