import xml.etree.ElementTree as ET
import requests

nyt_rss = "https://www.nytimes.com/services/xml/rss/nyt/HomePage.xml"

r = requests.get(nyt_rss, verify = False)

lines = r.text.splitlines()

lines = lines[1:]

with open("output.txt", "w") as file:
    file.write("\n".join(lines))

xml_doc = ET.parse("\n".join(lines))

root = xml_doc.getroot()

tag = len(root)

print(tag)
