xml_string = """
<data>
    <user>
        <name>123</name>
    </user>
    <user>
        <name>456</name>
    </user>
</data>
"""

import xml.etree.ElementTree as ET
root = ET.fromstring(xml_string)

result = root.findall("./user[name='123']")

# print(result.tag)