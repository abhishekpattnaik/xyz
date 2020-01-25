import pandas as pd
import xml.etree.ElementTree as ET
tree = ET.parse('XML test/deal1.xml')
root = tree.getroot()
inputQuery = str(input("Enter e string to be searched"))
for element in root.iter(inputQuery):
    print(element.text)