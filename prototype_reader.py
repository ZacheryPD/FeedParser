import xml.etree.ElementTree as ET
import requests

from pprint import pprint


class Article:
    def __init__(self):
        self.description = ""
        self.url = ""
        self.title = ""


    def __init__(self, xml_doc):
        self.description = xml_doc.find("description").text
        self.title = xml_doc.find("title").text
        self.url = xml_doc.find("link").text

    def __str__(self):
        return "title: {}\n\tdescription: {}\n\tlink: {}".format(self.title, self.description, self.url)

nyt_rss = "https://www.nytimes.com/services/xml/rss/nyt/HomePage.xml"

r = requests.get(nyt_rss, verify = False)

xml_doc = ET.fromstring(r.text)

tags = xml_doc.findall('channel/item')

pprint(tags[0])

article = Article(tags[0])

print(article)
