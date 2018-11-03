import requests


def analyze_picture(picture_path, engine="haystackai_demo"):
    url = "https://api.haystack.ai/api/image/analyze?output=json&limit=10000&apikey=c1ee6e8f5a8a2a26935e38d211a0e327"
    with open(picture_path, 'rb') as f:
        files = {'image': (picture_path, f.read(), 'image/jpeg')}
    headers = {
        "user-agent": "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36",
        "Host": "api.haystack.ai",
        "Origin": "https://www.haystack.ai",
        "Referer": "https://www.haystack.ai/demos/Yahoo-NSFW-Demo"}
    r = requests.post(url, files=files, headers=headers)
    return r.json()