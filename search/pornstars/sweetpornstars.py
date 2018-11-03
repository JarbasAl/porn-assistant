from bs4 import BeautifulSoup
import requests
from pprint import pprint


def get_pornstar_data(url="https://sweet-pornstars.com/abella-danger"):
    data = {"url": url,
            "picture": url.replace("https://sweet-pornstars.com/",
                                   "https://sweet-pornstars.com/assets/images/imgpornstars/") +".jpg",
            "categories": [],
            "models": []}
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')
    mydivs = soup.findAll('div')
    for div in mydivs:
        if div.get("itemprop", "") == "description":
            data["description"] = div.text
        elif div.get("class", "") == ["card-content", "red", "lighten-2"]:
            for line in div.text.split("\n"):
                if ":" in line:
                    attr, val = line.split(":")
                    data[attr.lower().replace(" ", "_").strip()] = val.strip()

    mydivs = soup.findAll('label')
    for div in mydivs:
        data[div.find('input')["name"]] = div.text.strip()
    return data


def get_pornstar_list(data=True):
    counter = 0
    pornstars = {}
    url = 'https://sweet-pornstars.com/pornstars/'
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')
    mydivs = soup.findAll('div')
    for div in mydivs:
        if div.get("class", "") == ['col', 's12', 'm4', 'l3']:
            counter += 1
            text = str(div)
            text = text.replace('<div class="col s12 m4 l3"><div class="collection" style="margin: .5rem 0;"><a class="collection-item" href="', "")
            s = text.find(">")
            e = text.find("<sup>")
            name = text[s+1:e].strip()
            url = "https://sweet-pornstars.com/" + name.replace(" ", "-").lower()
            if data:
                pornstars[name] = get_pornstar_data(url)
            else:
                pornstars[name] = {"url": url}
    print("found", counter, "pornstars")
    return pornstars

pprint(get_pornstar_list())