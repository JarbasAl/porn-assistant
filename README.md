# PA - Porn Assistant
[![Donate with Bitcoin](https://en.cryptobadges.io/badge/micro/1QJNhKM8tVv62XSUrST2vnaMXh5ADSyYP8)](https://en.cryptobadges.io/donate/1QJNhKM8tVv62XSUrST2vnaMXh5ADSyYP8)
[![Donate](https://img.shields.io/badge/Donate-PayPal-green.svg)](https://paypal.me/jarbasai)
<span class="badge-patreon"><a href="https://www.patreon.com/jarbasAI" title="Donate to this project using Patreon"><img src="https://img.shields.io/badge/patreon-donate-yellow.svg" alt="Patreon donate button" /></a></span>
[![Say Thanks!](https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg)](https://saythanks.io/to/JarbasAl)

Porn and gaming are at the forefront of technological innovation, this repo 
makes it easy for you to experiment with anything that is porn 
related, but we are in the 21st century, let's get AI in the mix!

This project aims to provide the tools for an intelligent assistant that 
learns your tastes and even recommends X-rated stuff you like, the less time 
you waste searching for videos the faster you get back to real work, or, you
 know, gaming

This package is also helpful for scrapping, we all know you never look at your 
offline collection, but dubious methods involving reuploading can turn a profit


NOTE: No porn included, find your own


NOTE2: This isn't finished, don't ask questions about it, feel free to look 
at the code, clean-ish and self explanatory i think


## Classifiers

So, i have no idea on what your killer 18+ app is about, but you likely will
 need to classify stuff, i assume pictures

- attractiveness
- ethnicity
- nsfw 
- nudity
- pornstar matching


you really shouldn't abuse this, since im scrapping some web demos, but hey,
 this is a hacker project, not a serious lib you should depend on
 
Are you curious if there's a pornstar that looks just like that crush of 
yours? wonder no more and get the closest one

     from classifiers.pornstar_matching import closest_pornstar
    from pprint import pprint
    
    data = closest_pornstar("instagram_picture.jpg")
    pprint(data)
 
There's even some urls to get you started
 
    {'name': 'Eve Lawrence',
     'score': 29,
     'urls': ['https://www.youporn.com/pornstar/770/eve-lawrence/',
              'https://www.pornhub.com/pornstar/eve-lawrence',
              'https://www.redtube.com/pornstar/eve+lawrence']}

## RAW data

if you are just looking into some juice data without real porn in there

    ├── categories_minimal.txt
    ├── keywords_small.txt
    ├── keywords.txt
    ├── pornhub
    │   ├── albums.json
    │   └── comments.json
    ├── pornstars_slutsinc.csv
    ├── sweet_pornstars.json
    ├── taxonomy.json
    ├── xnxx
    │   └── videos_raw.csv
    └── youporn
        ├── tags.csv
        └── videos_raw.csv


## Scrapping

You might need some actual porn to do stuff, you can search and scrap a 
bunch of sites

- Pornhub
- Xnxx
- Youporn

Getting pornstar data from pornhub has never been easier
 
If you want to check available pornstars
   
    for s in stars.get_stars_list(infinity=True):
        pprint(s)

You won't get a lot of data

    {'name': 'Lana Rhoades',
     'photo': 'https://ci.phncdn.com/pics/pornstars/000/255/751/(m=lciyeNbOb_c)(mh=ajL2jLz9Fgd3ehXU)thumb_1116181.jpg',
     'url': 'http://pornhub.com/pornstar/lana-rhoades',
     'videos': 624}
    {'name': 'Mia Khalifa',
     'photo': 'https://ci.phncdn.com/pics/pornstars/000/061/561/(m=lciyeNbOb_c)(mh=gnmb0ABkOm0Tmfsm)thumb_1148951.jpg',
     'url': 'http://pornhub.com/pornstar/mia-khalifa',
     'videos': 2660}
    {'name': 'Riley Reid',
     'photo': 'https://ci.phncdn.com/pics/pornstars/000/005/343/(m=lciyeNbOb_c)(mh=ztaGdHllNMKma_cI)thumb_646361.jpg',
     'url': 'http://pornhub.com/pornstar/riley-reid',
     'videos': 2068}

But you can search individual pornstars


    from search.pornhub.stars import Stars
    from pprint import pprint
    
    stars = Stars()
    for s in stars.search_star("adria rae"):
        pprint(s)
 
You will get plenty info this time
    
    {'age': '22',
     'aliases': ['Aspen Reign'],
     'background': 'American',
     'bio': '\n'
            '\n'
            '\n'
            'Fan fave Adria Rae, also known as Aspen Reign, is an extra-petite '
            'twenty-year-old Virgo from Michigan and one of the best-loved new '
            'girls in porn. NightMoves even gave Adria the 2016 award for Best New '
            'Starlet. A 5’5” brunette with tiny 34B tits perfect for biting, Adria '
            'only got started in porno in 2015, but she’s already got at least '
            'forty credits to her name. One of her pictures was a ‘fauxcest’ '
            'feature for Digital Sin, and recently she did her first IR bald '
            'creampie for Blacked. She’s also done girl-on-girl BDSM for Digital '
            'Sin, more ‘fauxcest’ for Mile High, anal for Tushed, and lots of teen '
            'scenes. With her long brown hair, hazel eyes, and heart-shaped face, '
            'Adria has classic sweetheart beauty. Don’t let her sweet face fool '
            'you, though. In addition to being a monster slut and self-proclaimed '
            '‘dab queen’, Adria is also fit AF and will deliver push-ups with '
            'military precision at a moment’s notice. Just check out her '
            'Instagram! Oh, and her prized cat Artemis even has an Instagram '
            'account! Adria interacts a lot with her fans on social media, so you '
            'can contact her via her personal Snapchat, and follow her on Insta, '
            'Twitter, and Tumblr. Or just stay right here on Pornhub and check out '
            'dozens of vids of Adria and her dirty deeds!\n'',
     'career start and end': 'to\n\t\t\t\t\t\t\t\tPresent',
     'career status': 'Active',
     'city and country': 'Los Angeles, US',
     'costars': ['Aaron Wilcox',
                 'Abby Lee Brazil',
                 'Alex D',
                 'Anissa Kate',
                 'Ariana Marie',
                 'Arya Fae',
                 'August Ames',
                 'Baby Jewel',
                 'Bella Rose',
                 'Blair Williams',
                 'Brad Knight',
                 'Buddy Hollywood',
                 'Cara Stone',
                 'Carter Cruise',
                 'Cassidy Klein',
                 'Charles Dera',
                 'Chloe Cherry',
                 'Daisy Monroe',
                 'Danica Dillan',
                 'Danny Mountain',
                 'Dick Chibbles',
                 'Elizabeth Jolie',
                 'Ella Knox',
                 'Elsa Jean',
                 'Hope Harper',
                 'India Summer',
                 'Iris Rose',
                 'Isiah Maxwell',
                 'James Deen',
                 'Jax',
                 'Jay Smooth',
                 'Jaye Summers',
                 'Jean Val Jean',
                 'Jenna Reid',
                 'Jill Kassidy'],
     'ethnicity': 'White',
     'gender': 'Female',
     'hair color': 'Brunette',
     'height': '5 ft 5 in (165 cm)',
     'hometown': 'Grand Rapids, Mi',
     'interested in': 'Girls',
     'measurements': '32B-25-33',
     'pornstar_uploaded_videos': {'Adria Rae & Gina Valentina Sexy Lesbian Vampire Nurses': 'http://pornhub.com/view_video.php?viewkey=ph5bd89cafe8bd8',
                                  'Adria Rae Anal Valentines Day: secret sextape': 'http://pornhub.com/view_video.php?viewkey=ph5abd72b9ee1e4',
                                  'Adria Rae secret Snapchat sextape': 'http://pornhub.com/view_video.php?viewkey=ph5a5bd6187806a',
                                  'Adria Raw solo masturbation': 'http://pornhub.com/view_video.php?viewkey=ph5a5f75b70b880',
                                  'STOLEN SNAPCHAT STORY FROM ADRIA RAES PREMIUM SNAPCHAT': 'http://pornhub.com/view_video.php?viewkey=ph5b6272fa30b9d',
                                  'Snapchat show': 'http://pornhub.com/view_video.php?viewkey=ph5b722e4ce9437'},
     'recent_videos': {'Adria Rae & Jax Slayher': 'http://pornhub.com/view_video.php?viewkey=ph5a3fef4d1b190',
                       'Adria Rae gets pounded by her new trainer’s BBC': 'http://pornhub.com/view_video.php?viewkey=ph5b239299398fb',
                       'EvilAngel Adria Rae Licks Daddy’s Ass Takes Anal & 2 Creampies': 'http://pornhub.com/view_video.php?viewkey=ph5bbf5863c88ff',
                       'Family Threesome With Step-Mom': 'http://pornhub.com/view_video.php?viewkey=ph5b736622a7a13',
                       'Lesbian Teen Masseuse Adria Rae Visited By Angry Red Head Wife': 'http://pornhub.com/view_video.php?viewkey=ph5b437defa9386',
                       "Petite Adria Rae Takes Big Cock On Daddy's Pool Table S28:E9": 'http://pornhub.com/view_video.php?viewkey=ph5bc11e9f7e6c8',
                       'SWALLOWED Five sexy babe gagging on lucky dudes fat cock': 'http://pornhub.com/view_video.php?viewkey=ph594b9f9d3800b',
                       "StepSister Catfight Leads to Fucking in Dad's Office!": 'http://pornhub.com/view_video.php?viewkey=ph5b32450a71623',
                       'TRUE ANAL Petite Adria Rae has her butt stuffed by a big cock': 'http://pornhub.com/view_video.php?viewkey=ph5b8fee3026f85',
                       "TUSHY Naughty Teen Craves Her Friend's BF's Cock": 'http://pornhub.com/view_video.php?viewkey=ph5aa246bf33415',
                       'Twistys - A Treat Story Fortunate One Part 3 - Adria Rae': 'http://pornhub.com/view_video.php?viewkey=ph5b295d1bbfa0a',
                       "Young submissive slut Adria Rae gets deeply pounded and creampied by 'John'": 'http://pornhub.com/view_video.php?viewkey=ph5bc22acd5e0c4'},
     'relationship status': 'Single',
     'social_networks': {'Official Site': 'http://adriarae.com',
                         'Twitter': 'https://twitter.com/adriaxrae'},
     'weight': '110 lbs (50 kg)'}
     
## Models

You need to model your porn data in a sane way to do something useful, i 
made some classes to work with

- Pornstars
- Videos
- Tags

