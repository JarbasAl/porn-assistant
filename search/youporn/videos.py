import urllib.request, urllib.error, urllib.parse
from bs4 import BeautifulSoup
from db import PornMedia


class YoupornVideo(PornMedia):
    '''
    Set up simple video-class
    '''

    def __init__(self):
        self.url = ""
        self.tags = []
        self.categories = []
        self.length = "-"
        self.date = "-"

    def __repr__(self):
        return "%s, Tags: %s, Categories: %s, %s, %s" % (
        self.url, str(self.tags), str(self.categories), self.length, self.date)


def get_youporn_video(videourl):
    video = YoupornVideo()  # initialize new video
    try:  # failsafe: youporn is great in giving links to broken URLs which crash everything.
        opener = urllib.request.build_opener()
        opener.addheaders.append(("Cookie", "age_verified=1"))
        url = opener.open(videourl)
        urlcontent = url.read()  # read content
        soup = BeautifulSoup(urlcontent, "xml")  # parse using the xml-parser & beautiful soup
        video.url = str(videourl)
        length_date = soup.find("ul", {"class": "spaced"}).findAll("li")
        for element in length_date:
            if element.getText().find("Duration:") != -1:
                video.length = element.getText()[element.getText().find("Duration:") + 10:]
            elif element.getText().find("Date:") != -1:
                video.date = element.getText()[element.getText().find("Date:") + 6:]
        tag_elements = soup.findAll("ul", {"class": "listCat"})
        for tag_element in tag_elements:
            if str(tag_element.b.text) == "Categories:":
                elements = tag_element.findAll("a")
                for element in elements:
                    video.categories.append(str(element.string))
            elif str(tag_element.b.text) == "Tags:":
                elements = tag_element.findAll("a")
                for element in elements:
                    video.tags.append(str(element.string))
    except:
        pass
    return video
