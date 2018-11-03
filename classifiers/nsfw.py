import requests
from settings import HAYSTACKAI_KEY


def open_nsfw(picture_path, engine="haystackai_demo"):
    return haystack_nsfw_demo(picture_path)


def haystack_nsfw_demo(picture_path):
    url = "https://api.haystack.ai/api/image/analyze?output=json&limit=10000&model=nudity&apikey=" + HAYSTACKAI_KEY
    with open(picture_path, 'rb') as f:
        files = {'image': (picture_path, f.read(), 'image/jpeg')}
    headers = {
        "user-agent": "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36",
        "Host": "api.haystack.ai",
        "Origin": "https://www.haystack.ai",
        "Referer": "https://www.haystack.ai/demos/Yahoo-NSFW-Demo"}
    r = requests.post(url, files=files, headers=headers)
    return r.json()
