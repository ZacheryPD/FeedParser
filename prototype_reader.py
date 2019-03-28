import xml.etree.ElementTree as ET
import requests

nyt_rss = "https://www.nytimes.com/services/xml/rss/nyt/HomePage.xml"

r = requests.get(nyt_rss, verify = False)

xml_doc = ET.fromstring(r.text)

tags = xml_doc.findall('channel/item')

print(len(tags))
