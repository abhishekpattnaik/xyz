import pandas as pd
import xml.etree.ElementTree as ET
tree = ET.parse('XML test/log1.xml')
root = tree.getroot()
D = {}
dataFrame = pd.DataFrame()
L =[]
for parentElement in root:
    for childElement in parentElement:
        D[childElement.tag]=childElement.text
print(dataFrame)