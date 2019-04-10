class Article:
    def __init__(self):
        self.description = ""
        self.url = ""
        self.title = ""
        self.published_date = ""

    def __str__(self):
        return "title: {}\n\tdescription: {}\n\tlink: {}\n\tpublished_date: {}".format(self.title, self.description, self.url, self.published_date)

class Image:
   def __init__(self):
       self.title = ""
       self.url = ""
       self.link = ""

class Feed:
    def __init__(self):
        self.image = Image()
        self.articles = []

        self.link = ""
        self.last_build_date = ""
        self.title = ""

    def __str__(self):
        return "{} \n\t- link:{}\n\t- last_build_date: {}\n\t- {} article(s)".format(self.title, self.link, self.last_build_date, len(self.articles))

class ArticleParser:
    def parse(self, xml_doc):
        article = Article()

        article.description = xml_doc.find("description").text
        article.title = xml_doc.find("title").text
        article.url = xml_doc.find("link").text
        article.published_date = xml_doc.find("pubDate").text

        return article

class ImageParser:
    def parse(self, xml_doc):
        image = Image()

        image.title = xml_doc.find('title').text
        image.url = xml_doc.find('url').text
        image.link = xml_doc.find('link').text

        return image

class FeedParser:
    def __init__(self, ):
        self.image_parser = ImageParser()
        self.article_parser = ArticleParser()


    def parse(self, xml_doc):
        feed = Feed()

        feed.image = self.image_parser.parse(xml_doc.find('image'))
        feed.articles = [self.article_parser.parse(article_doc) for article_doc in xml_doc.findall('item')]

        feed.link = xml_doc.find('link').text
        feed.last_build_date = xml_doc.find('lastBuildDate').text
        feed.title = xml_doc.find('title').text

        return feed
