import xml.etree.ElementTree as ET
import requests

from pprint import pprint


class Article:
    def __init__(self):
        self.description = ""
        self.url = ""
        self.title = ""
        self.published_date = ""


    def __init__(self, xml_doc):
        self.description = xml_doc.find("description").text
        self.title = xml_doc.find("title").text
        self.url = xml_doc.find("link").text
        self.published_date = xml_doc.find("pubDate").text

    def __str__(self):
        return "title: {}\n\tdescription: {}\n\tlink: {}\n\tpublished_date: {}".format(self.title, self.description, self.url, self.published_date)

class Image:
   def __init__(self):
       self.title = ""
       self.url = ""
       self.link = ""

   def __init__(self, xml_doc):
       self.title = xml_doc.find('title').text
       self.url = xml_doc.find('url').text
       self.link = xml_doc.find('link').text

class Feed:
    def __init__(self):
        self.image = Image()
        self.articles = []

        self.link = ""
        self.last_build_date = ""
        self.title = ""

    def __init__(self, xml_doc):
        self.image = Image(xml_doc.find('image'))
        self.articles = [Article(article_doc) for article_doc in xml_doc.findall('item')]

        self.link = xml_doc.find('link').text
        self.last_build_date = xml_doc.find('lastBuildDate').text
        self.title = xml_doc.find('title').text

    def __str__(self):
        return "{} \n\t- link:{}\n\t- last_build_date: {}\n\t- {} article(s)".format(self.title, self.link, self.last_build_date, len(self.articles))


nyt_rss = "https://www.nytimes.com/services/xml/rss/nyt/HomePage.xml"

r = requests.get(nyt_rss, verify = False)

xml_doc = ET.fromstring(r.text)

nyt_feed = Feed(xml_doc.find("channel"))

print(nyt_feed)

print(nyt_feed.articles[3])
