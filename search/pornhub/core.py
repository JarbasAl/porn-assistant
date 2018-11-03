# -*- coding: UTF-8 -*-
from search.pornhub import *


# too many request in short time will result in firewall block

def is_album(url):
    """
    Validate album url
    www.pornhub.com/album/show_album?id=SOMENUMBERS
    """
    return True if ALBUM_URL in url else False


def is_photo_preview(url):
    """
    Validate photo preview url
    In albums only photo preview url can be found, not the actual url
    www.pornhub.com/photo/SOMENUMBERS
    """
    return True if PHOTO_PREVIEW in url else False


def is_photo(url):
    """
    Validate photo full url
    i1.cdn2b.image.pornhub.phncdn.com/pics/albums/SOMENUMBERS/SOMETEXT.jpg
    """
    return True if (ALBUM_PHOTO_URL in url) and (url[-4:] == PHOTO_EXT) else False


def is_star(url):
    """
    Validate pornstar's page
    www.pornhub.com/pornstar/SOMENAME
    """
    return True if PORNSTAR_URL in url else False


def is_star_photo(url):
    """
    Validate pornstar's profile photo
    i0.cdn2a.image.pornhub.phncdn.com/pics/pornstars/SOMENUMBERS/SOMETEXT.jpg
    """
    return True if (PORNSTAR_PHOTO in url) and (url[-4:] == PHOTO_EXT) else False


def is_video(url):
    """
    Validate video url
    www.pornhub.com/view_video.php?viewkey=SOMETEXT
    """
    return True if VIDEO_URL in url else False


def is_video_photo(url):
    """
    Validate video background photo
    i0.cdn2b.image.pornhub.phncdn.com/videos/SOMENUMBERS/SOMETEXT.jpg
    """
    return True if (VIDEO_IMAGE_URL in url) and (url[-4:] == PHOTO_EXT) else False


