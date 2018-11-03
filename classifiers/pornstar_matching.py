import requests
from bs4 import BeautifulSoup


def closest_pornstar(picture_path, engine="pornstarbyface"):
    return pornstarbyface(picture_path)


def pornstarbyface(face_picture):
    data = {}
    url = "https://pornstarbyface.com/Home/LooksLikeByPhoto"
    with open(face_picture, 'rb') as f:
        files = {'imageUploadForm': (face_picture, f.read(), 'image/jpeg')}
    r = requests.post(url, files=files)
    html = r.text
    soup = BeautifulSoup(html, 'html.parser')
    mydivs = soup.findAll('div')
    score = 0
    for div in mydivs:
        urls = []
        if "progress-bar" in div.get("class", []):
            score = int(div["similarity"])
        elif div.get("class", "") == ["candidate-real"]:
            for d in div.findAll("div"):
                p = d.find("p")
                name = p.text
                for a in d.findAll("a"):
                    urls.append(a["href"])
                data = {"name": name, "urls": urls, "score": score}

    return data
