from article import FeedParser

import xml.etree.ElementTree as ET
import requests

from pprint import pprint

feed_parser = FeedParser()

nyt_rss = "https://www.nytimes.com/services/xml/rss/nyt/HomePage.xml"

r = requests.get(nyt_rss, verify = False)

xml_doc = ET.fromstring(r.text)

nyt_feed = feed_parser.parse(xml_doc.find("channel"))

print(nyt_feed)

print(nyt_feed.articles[3])
