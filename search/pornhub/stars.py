# -*- coding: UTF-8 -*-
from search.pornhub import *
from search.pornhub.core import is_star, is_star_photo
from bs4 import BeautifulSoup
import requests


class Stars(object):

    def __init__(self, *args):
        pass

    def _load_stars_page(self, page_num):
        payload = {"page": page_num}
        r = requests.get(BASE_URL + PORNSTARS_URL, params=payload,
                         headers=HEADERS)

        return BeautifulSoup(r.text, "html.parser")

    def _scrap_li_stars(self, soup_data):
        # get div with list of stars (month popular is the 1st)
        div_el = soup_data.findAll("div", {"class": "sectionWrapper",
                                           "id": "pornstarsFilterContainer"})[
            0]
        # get each porn pornstar info (held in list block)
        li_el = div_el.find_all("li")

        return li_el

    def _scrap_star_info(self, li_el):
        data = {
            "name": None,  # string
            "url": None,  # string
            "photo": None,  # string
            "videos": None  # integer
        }

        # scrap url
        for a_tag in li_el.find_all("a", href=True):
            try:
                url = a_tag.attrs["href"]

                if is_star(url):
                    data["url"] = BASE_URL + url
                    break
            except Exception as e:
                pass

        # scrap name and photo url
        for img_tag in li_el.find_all("img", src=True):
            try:
                photo_url = img_tag.attrs["data-thumb_url"]
                if is_star_photo(photo_url):
                    data["photo"] = photo_url
                    data["name"] = img_tag.attrs["alt"]
                    break
            except Exception as e:
                pass

        # scrap num of videos
        for span_tag in li_el.find_all("span", {"class": "videosNumber"}):
            try:
                data["videos"] = int(str(span_tag).split(">")[1].split(" ")[0])
                break
            except Exception as e:
                pass

        # scrap data
        bio = li_el.find_all("div", {"class": "claimed withBio"})
        # return
        return data if None not in data.values() else False

    def _scrap_star_page(self, soup):
        data = {"bio": ""}
        # pornstar bio
        if soup.find("div", {"class": "bio"}):
            data["bio"] = soup.find("div", {"class": "bio"}).text.replace(
                "Bio\n", "")
        # key: data   fields
        for a in soup.find_all("div", {"class": "infoPiece"}) or []:
            k, d = a.text.split(":")
            data[k.strip().lower()] = d.strip()

        # recent videos for pornstars pages
        soupb = soup.find("div", {"class": "sectionWrapper"})
        vids = {}
        for v in soupb.find_all("div", {"class": "wrap"}) or []:
            v = v.find("a")
            title = v.attrs["title"]
            url = BASE_URL + v.attrs["href"]
            vids[title] = url
        data["recent_videos"] = vids
        data["pornstar_uploaded_videos"] = {}

        # some stars are users , videos will be in different divs
        if not len(vids):
            soupb = soup.find("div", {
                "class": "sectionWrapper pornstarUploadedVideos"})
            vids = {}
            for v in soupb.find_all("div", {"class": "wrap"}) or []:
                v = v.find("a")
                title = v.attrs["title"]
                url = BASE_URL + v.attrs["href"]
                vids[title] = url
            data["pornstar_uploaded_videos"] = vids
            soupb = soup.find("div",
                              {
                                  "class": "sectionWrapper mostRecentPornstarVideos"})
            vids = {}
            for v in soupb.find_all("div", {"class": "wrap"}) or []:
                v = v.find("a")
                title = v.attrs["title"]
                url = BASE_URL + v.attrs["href"]
                vids[title] = url
            data["recent_videos"] = vids

        # social networks
        social_networks = {}
        soupb = soup.find("div", {"class": "contentContainer about"})
        if soupb:
            for v in soupb.find_all("a",
                                    {"class": "js-ckeckExternalSource"}) or []:
                if not v.attrs["href"].startswith("http"):
                    continue  # pass internal porn hub sites (ask a pornstar, jules jordan, smash pictures...)
                social_networks[v.text.strip()] = v.attrs["href"]

        data["social_networks"] = social_networks

        # alternate names
        if soup.find("div", {"class": "aliases"}):
            data["aliases"] = [s.strip() for s in soup.find("div", {
                "class": "aliases"}).text.replace("\t", "").replace(
                "Also Known As", "").split(",")]
        else:
            data["aliases"] = []

        # cleanup some "bad" data scrapped together
        bads = ["joined", "pornstar profile views", "videos watched",
                "profile views"]
        for b in bads:
            if b in data:
                data.pop(b)
        return data

    def _get_costars(self, soup):
        costars = []
        if soup:
            for s in soup.find_all("a", {"class": "title js-mxp"}):
                costars.append(s.text)
        return costars

    def get_stars_list(self, quantity=20, page=1, infinity=False):
        """
        Get pornstar's basic informations.

        :param quantity: number of pornstars to return
        :param page: starting page number
        :param infinity: never stop downloading
        """

        quantity = quantity if quantity >= 1 else 1
        page = page if page >= 1 else 1
        found = 0

        while True:

            for possible_star in self._scrap_li_stars(self._load_stars_page(
                    page)):
                data_dict = self._scrap_star_info(possible_star)
                if data_dict:
                    yield data_dict

                    if not infinity:
                        found += 1
                        if found >= quantity: return

            page += 1

    def search_star(self, name, quantity=1, page=1, infinity=False):
        quantity = quantity if quantity >= 1 else 1
        page = page if page >= 1 else 1
        found = 0

        while True:
            payload = {"page": page, "search": name}
            r = requests.get(BASE_URL + PORNSTARS_URL + "/search",
                             params=payload,
                             headers=HEADERS)

            soup = BeautifulSoup(r.text, "html.parser")
            div_el = soup.find_all("div", {"class": "wrap"})
            for possible_star in div_el:
                data_dict = self._scrap_star_info(possible_star)
                if data_dict:
                    url = data_dict["url"]

                    r = requests.get(url, headers=HEADERS)
                    soup = BeautifulSoup(r.text, "html.parser")
                    data = self._scrap_star_page(soup)

                    r = requests.get(url + "/costars",
                                     headers=HEADERS)
                    soup = BeautifulSoup(r.text, "html.parser")
                    div_el = soup.find("div", {"class": "coStars claimed"})
                    data["costars"] = self._get_costars(div_el)

                    yield data
                    if not infinity:
                        found += 1
                        if found >= quantity: return

            page += 1
