# http://www.barelist.com/search/model.aspx
def search_by_spec(params=None):
    params = params or {
        "profession": {"pornstar": True, "centerfold": True},
        "ethnicity": {"caucasian": True},
        "age": {"18-21": True, "22-25": True, "26-30":True},
        "cup_size": {"A":True, "B": True, "C": True, "D": True},
        "hair_color": {"Blonde": True, "Brunette": True, "Black": True, "Red": True},
        "height": {"152cm": True,  "152-157cm":True, "157-165cm": True, "165-172cm": True, "176-182cm": True, "182cm": True},
        "weight": {"45": True, "45-50": True, "50-54": True, "54-59": True}
    }


#http://www.barelist.com/search/galleries.aspx
def search_gallery(params=None):
    params = params or {
        "gallery_type": {"pictures": True, "videos": True, "hardcore": True, "softcore": True},
        "profession": {"pornstar": True, "centerfold": True},
        "ethnicity": {"caucasian": True},
        "age": {"18-21": True, "22-25": True, "26-30": True},
        "cup_size": {"A": True, "B": True, "C": True, "D": True},
        "hair_color": {"Blonde": True, "Brunette": True, "Black": True, "Red": True},
        "height": {"152cm": True, "152-157cm": True, "157-165cm": True, "165-172cm": True, "176-182cm": True,
                   "182cm": True},
        "weight": {"45": True, "45-50": True, "50-54": True, "54-59": True}
    }