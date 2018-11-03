import urllib.request, urllib.error, urllib.parse
import pickle
import search.xnxx.videos
from bs4 import BeautifulSoup


def videos_for_page(url):
    '''
    Grab all PornMedia-Links from single tag-page, like
    http://video.xnxx.com/tags/acrobat
    '''
    url = urllib.request.urlopen(url)
    urlcontent = url.read()
    soup = BeautifulSoup(urlcontent, "xml")
    video_urls = []
    for a in soup.findAll("a"):  # iterate over all <a></a>-tags in soup. Return link to video if found
        if "class" in a:
            if a["class"] == "miniature":
                video_urls.append(a["href"])
    return video_urls


def iterate_videos(url):
    '''
    Iterate over all video-pages for a single tag. E.g. get "acrobat"-videos
    from page 1 to 8:  
    '''
    url = urllib.request.urlopen(url)  # again, reading the site
    urlcontent = url.read()
    soup = BeautifulSoup(urlcontent, "xml")
    video_urls = []
    video_urls.extend(videos_for_page(soup))  # give soup to function to find all videos on initial page
    next_url = ""
    next = False
    print(len(video_urls))
    for i in soup.findAll("a",
                          "nP"):  # check whether there are more pages to grab. if yes return url of next page and set flag to True
        if i.string == "Next":
            next = True
            next_url = "http://video.xnxx.com" + i["href"]
            break
        else:
            next = False

    while next == True:  # if there are more pages in forward direction: grab those as well.

        video_urls.extend(videos_for_page(next_url))
        print(len(video_urls))
        for i in soup.findAll("a", "nP"):
            if i.string == "Next":
                next = True
                next_url = "http://video.xnxx.com" + i["href"]
                break
            else:
                next = False
    return video_urls


def get_tag_videos(tag_url, video_collection=None):
    '''
    Iterate over all videos in array and return a dictionary with
    key = videourl, value = video-object, see videos.py
    '''
    video_collection = video_collection or {}
    print("getting video-urls for tag")
    video_urls = iterate_videos(tag_url)
    print("got video-urls")
    print("getting tag-collection for all videos")
    for video in video_urls:
        if (video in video_collection) == False:
            print("saving " + video)
            video_tags = search.xnxx.videos.get_xnxx_video(video)
            video_collection[video_tags.url] = video_tags
        else:
            print("skipped " + video + " as already saved")
    print("got all videos for tag")
    return video_collection


def get_tags(url="http://video.xnxx.com/tags/"):
    '''
    Set up initial tag-list from URL. 
    Take http://video.xnxx.com/tags/ and iterate over all tags and get list of links to each tag
    '''
    url = urllib.request.urlopen(url)
    urlcontent = url.read()
    soup = BeautifulSoup(urlcontent, "xml")
    invalid_tags = ["/tags/", "/tags/", "/tags/-", "/tags/--", "/tags/---"]
    tags = {}
    for a in soup.findAll("a"):
        if "href" in a:
            if a["href"].find("/tags/") != -1 and a["href"] not in invalid_tags:
                tags[str(a["href"])] = False
    return tags


def _iIterate_tags(url):
    '''
    Load or get all tags, iterate over each tag to get videos & tags
    '''
    try:
        video_pickle = open("video_collection.pickle",
                            "rb")  # if we already ran the script there should be videos to save
        video_collection = pickle.load(video_pickle)
        video_pickle.close()
        print("loaded saved videos")
    except:
        print("created new video-collection")  # if not create new collection
        video_collection = {}
    try:
        tag_pickle = open("tag_collection.pickle", "rb")  # same is true for tags
        tag_collection = pickle.load(tag_pickle)
        tag_pickle.close()
        print("loaded tag-collection")
    except:
        print("getting new tags")
        tag_collection = get_tags(url)
        print("got new tags")
    counter = 0
    for tag, value in tag_collection.items():  # now iterate over each tag
        if value == False:  # if it already was parsed (value == True: great, we skip it)
            print("############################################")
            print("iterate over videos for %s" % (tag))
            video_collection = get_tag_videos(video_collection, "http://video.xnxx.com" + tag)
            print("got all videos for %s" % (tag))
            tag_collection[tag] = True
            print(tag_collection[tag])
            if counter % 100 == 0 and counter != 0:
                video_pickle = open("video_collection.pickle", "wb")
                tag_pickle = open("tag_collection.pickle", "wb")
                pickle.dump(tag_collection, tag_pickle)
                print("Saved Tag-Collection")
                pickle.dump(video_collection, video_pickle)
                print("Saved PornMedia Collection")
                tag_pickle.close()
                video_pickle.close()
            counter += 1
            print("Tags since last save: " + str(counter))
            print("Now got " + str(len(video_collection)) + " videos")
    print("Now got " + str(len(video_collection)) + " videos")
    print("############################################")
    video_pickle = open("video_collection.pickle", "wb")
    tag_pickle = open("tag_collection.pickle", "wb")
    pickle.dump(tag_collection, tag_pickle)
    print("Saved Tag-Collection")
    pickle.dump(video_collection, video_pickle)
    print("Saved PornMedia Collection")
    tag_pickle.close()
    video_pickle.close()
    print("Finished Crawling Data")
