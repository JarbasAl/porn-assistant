# -*- coding: UTF-8 -*-
from search.pornhub import *
from search.pornhub.core import is_video, is_video_photo
from bs4 import BeautifulSoup
import requests


class Videos(object):

    def __init__(self, keywords=None, *args):
        self.keywords = keywords or []

    def _craft_video_url(self, page_num):
        # url example:
        # pornhub.com/video/search?search=arg1+arg2
        # pornhub.com/video/search?search=arg1+arg2&p=professional
        # pornhub.com/video/search?search=arg1+arg2&p=professional&page=3

        payload = {"search": "", "page": page_num}

        for item in self.keywords:
            if (item == "professional") or (item == "pro"):
                payload["p"] = "professional"
            elif (item == "homemade") or (item == "home"):
                payload["p"] = "homemade"
            else:
                payload["search"] += (item + " ")

        return payload

    def _load_videos_page(self, page_num):
        r = requests.get(BASE_URL + VIDEOS_URL,
                         params=self._craft_video_url(page_num),
                         headers=HEADERS)
        html = r.text

        return BeautifulSoup(html, "lxml")

    def _scrap_li_videos(self, soup_data):
        return soup_data.find_all("li", {"class": "videoblock videoBox"})

    def _scrap_video_info(self, div_el):
        data = {
            "name": None,  # string
            "url": None,  # string
            "rating": None,  # integer
            "duration": None,  # string
            "background": None  # string
        }

        # scrap url, name
        for a_tag in div_el.find_all("a", href=True):
            try:
                url = a_tag.attrs["href"]
                if is_video(url):
                    data["url"] = BASE_URL + url
                    data["name"] = a_tag.attrs["title"]
                    break
            except Exception as e:
                pass

        # scrap background photo url
        for img_tag in div_el.find_all("img", src=True):
            try:
                url = img_tag.attrs["data-mediumthumb"]
                if is_video_photo(url):
                    data["background"] = url
                    break
            except Exception as e:
                pass

        # scrap duration
        for var_tag in div_el.find_all("var", {"class": "duration"}):
            try:
                data["duration"] = str(var_tag).split(">")[-2].split("<")[-2]
                break
            except Exception as e:
                pass

        # scrap rating
        for div_tag in div_el.find_all("div", {"class": "value"}):
            try:
                data["rating"] = int(str(div_tag).split(">")[1].split("%")[0])
                break
            except Exception as e:
                pass

        # return
        return data if None not in data.values() else False

    def get_videos(self, quantity=1, page=1, infinity=False):
        """
        Get videos basic informations.

        :param quantity: number of videos to return
        :param page: starting page number
        :param infinity: never stop downloading
        """

        quantity = quantity if quantity >= 1 else 1
        page = page if page >= 1 else 1
        found = 0

        while True:

            for possible_video in self._scrap_li_videos(
                    self._load_videos_page(page)):
                data_dict = self._scrap_video_info(possible_video)

                if data_dict:
                    yield data_dict

                    if not infinity:
                        found += 1
                        if found >= quantity: return

            page += 1
