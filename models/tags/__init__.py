t = """{


                    "physical":
                        {
                            "body": {"piercing": {"url": ""},
                                     "skin": {"type": {"pale": {"url": ""},
                                                       "tanned": {"tan lines": {
                                                           "url": "https://en.wikipedia.org/wiki/tan_line"},
                                                           "url": "https://en.wikipedia.org/wiki/sun_tanning"},
                                                       "url": ""},
                                              "url": ""},
                                     "tatoo": {"url": ""},
                                     "type": {"athletic": {"url": ""},
                                              "bbw": {"url": "https://fr.wikipedia.org/wiki/bbw"},
                                              "skinny": {"url": ""},
                                              "url": ""},
                                     "url": ""},
                            "breast": {"size": {"big breast": {"url": ""},
                                                "medium breast": {"url": ""},
                                                "small breast": {"url": ""},
                                                "url": ""},
                                       "type": {
                                           "enhanced": {"url": "https://en.wikipedia.org/wiki/breast_enlargement"},
                                           "natural": {"url": ""},
                                           "url": ""},
                                       "url": ""},
                            "hair": {"color": {"blonde": {"url": "https://en.wikipedia.org/wiki/blond"},
                                               "brunette": {"url": "https://en.wikipedia.org/wiki/brown_hair"},
                                               "redhead": {"url": "https://en.wikipedia.org/wiki/red_hair"},
                                               "url": ""},
                                     "size": {"long hair": {"url": "https://en.wikipedia.org/wiki/long_hair"},
                                              "short hair": {"url": "https://en.wikipedia.org/wiki/short_hair"},
                                              "url": ""},
                                     "type": {"curly": {"url": "https://en.wikipedia.org/wiki/hair#curly_hair"},
                                              "straight": {
                                                  "url": "https://en.wikipedia.org/wiki/hair#straight_hair"},
                                              "url": ""},
                                     "url": ""},
                            "url": ""},
                    "url": ""},
                                              
"""


class PornTag(object):
    name = "pornography tag"
    url = ""


class PornModel(PornTag):
    name = "pornography model"
    url = "https://en.wikipedia.org/wiki/Pornographic_film_actor"


class PhysicalAspect(PornModel):
    name = "pornography model physical aspect"
    url = ""


class Body(PhysicalAspect):
    name = "pornography model body"
    url = ""


class Hair(PhysicalAspect):
    name = "pornography model hair"
    url = ""


class Breast(PhysicalAspect):
    name = "pornography model breast"
    url = ""


class PornModelEthnicity(PornModel):
    name = "pornography model ethnicity"
    url = ""


class Ebony(PornModelEthnicity):
    name = "black pornstar"
    url = ""


class Caucasian(PornModelEthnicity):
    name = "caucasian pornstar"
    url = ""


class Asian(PornModelEthnicity):
    name = "asian pornstar"
    url = ""


class PornModelAge(PornModel):
    name = "pornography model age"
    url = ""


class Mature(PornModelAge):
    name = "mature pornstar"
    url = ""


class Teen(PornModelAge):
    name = "teen pornstar"
    url = ""


class PornModelGender(PornModel):
    name = "pornography model Gender"
    url = ""


class FemalePornModel(PornModelGender):
    name = "female pornography model"
    url = "https://en.wikipedia.org/wiki/Category:Pornographic_film_actresses"


class MalePornModel(PornModelGender):
    name = "male pornography model"
    url = ""


class PornGenre(PornTag):
    name = "pornography genre"
    url = ""


class SexualInterest(PornGenre):
    name = "sexual interest"
    url = ""


class Fetishism(SexualInterest):
    name = "fetishism"
    url = ""


class ClothingFetish(Fetishism):
    name = "clothing fetish"
    url = ""


class NonRestrictiveClothing(ClothingFetish):
    name = "non restrictive clothing fetishism"
    url = ""


class RestrictiveClothing(ClothingFetish):
    name = "restrictive clothing fetishism"
    url = ""


class Uniform(NonRestrictiveClothing):
    name = "uniform fetishism"
    url = "https://en.wikipedia.org/wiki/uniform_fetishism"


class School(Uniform):
    name = "school fetishism"
    url = ""


class Military(School):
    name = "military fetishism"
    url = ""


class Teacher(School):
    name = "teacher fetishism"
    url = ""


class Student(School):
    name = "student fetishism"
    url = ""


class Cheerleader(School):
    name = "cheerleader fetishism"
    url = "https://en.wikipedia.org/wiki/cheerleading"


class Office(Uniform):
    name = "office fetishism"
    url = ""


class Secretary(Office):
    name = "secretary fetishism"
    url = ""


class Boss(Office):
    name = "boss fetishism"
    url = ""


class Nurse(Uniform):
    name = "nurse fetishism"
    url = "https://en.wikipedia.org/wiki/nursing"


class Maid(Uniform):
    name = "maid fetishism"
    url = "https://en.wikipedia.org/wiki/maid"


class FabricType(NonRestrictiveClothing):
    name = "fabric type fetishism"
    url = ""


class Jeans(FabricType):
    name = "jeans fetishism"
    url = "https://en.wikipedia.org/wiki/jeans"


class Latex(FabricType):
    name = "latex fetishism"
    url = "https://en.wikipedia.org/wiki/latex_and_pvc_fetishism"


class Leather(FabricType):
    name = "leather fetishism"
    url = ""


class Spandex(FabricType):
    name = "spandex fetishism"
    url = "https://en.wikipedia.org/wiki/spandex"


class ClothingType(NonRestrictiveClothing):
    name = "clothing type fetishism"
    url = ""


class Lingerie(ClothingType):
    name = "Lingerie fetishism"
    url = ""


class ThighHighs(Lingerie):
    name = "thigh-highs fetishism"
    url = ""


class Stockings(Lingerie):
    name = "stockings fetishism"
    url = "https://en.wikipedia.org/wiki/stockings"


class PantyHose(Lingerie):
    name = "panty hose"
    url = "https://en.wikipedia.org/wiki/pantyhose"


class Shoes(ClothingType):
    name = "shoes fetishism"
    url = ""


class Sneakers(Shoes):
    name = "sneakers fetishism"
    url = "https://en.wikipedia.org/wiki/sneakers_footwear"


class HighHeels(Shoes):
    name = "high heels fetishism"
    url = "https://en.wikipedia.org/wiki/high-heeled_footwear"


class Boots(Shoes):
    name = "boots fetishism"
    url = ""


class Trousers(ClothingType):
    name = "trousers fetishism"
    url = "https://en.wikipedia.org/wiki/trousers"


class Shorts(ClothingType):
    name = "shorts fetishism"
    url = ""


class BDSM(Fetishism):
    name = "bdsm"
    url = "https://en.wikipedia.org/wiki/bdsm"


class FemaleDomination(BDSM):
    name = "female domination"
    url = "https://en.wikipedia.org/wiki/BDSM#Terminology_and_subtypes"


class Spanking(BDSM):
    name = "spanking"
    url = "https://en.wikipedia.org/wiki/spanking"


class Bondage(BDSM):
    name = "bondage"
    url = "https://en.wikipedia.org/wiki/bondage"


class Blindfolded(BDSM):
    name = "blindfolded"
    url = "https://en.wikipedia.org/wiki/blindfold"


class BodyFetish(Fetishism):
    name = "body"
    url = ""


class FootFetish(BodyFetish):
    name = "foot fetishism"
    url = "https://en.wikipedia.org/wiki/podophilia"


class Voyeurism(SexualInterest):
    name = "voyeurism"
    url = "https://en.wikipedia.org/wiki/voyeurism"


class Exhibitionism(SexualInterest):
    name = "exhibitionism"
    url = "https://en.wikipedia.org/wiki/exhibitionism"


class Streaking(Exhibitionism):
    name = "streaking"
    url = "https://en.wikipedia.org/wiki/streaking"


class Mooning(Exhibitionism):
    name = "mooning"
    url = "https://en.wikipedia.org/wiki/mooning"


class Flashing(Exhibitionism):
    name = "flashing"
    url = ""


class Candaulism(Exhibitionism):
    name = "anasyrma"
    url = "https://en.wikipedia.org/wiki/candaulism"


class Anasyrma(Exhibitionism):
    name = "anasyrma"
    url = "https://en.wikipedia.org/wiki/anasyrma"


class SexualPosition(PornGenre):
    name = "sexual position/act"
    url = ""


class NonPenetrative(SexualPosition):
    name = "non penetrative positions/acts"
    url = ""


class Titjob(NonPenetrative):
    name = "mammary intercourse"
    url = "https://en.wikipedia.org/wiki/mammary_intercourse"


class Handjob(NonPenetrative):
    name = "handjob"
    url = "https://en.wikipedia.org/wiki/handjob"


class Footjob(NonPenetrative):
    name = "footjob"
    url = "https://en.wikipedia.org/wiki/footjob"


class Penetrative(SexualPosition):
    name = "penetrative positions/acts"
    url = ""


class ExclusivelyPenetrative(Penetrative):
    name = "exclusively penetrative positions/acts"
    url = ""


class DoggyStyle(ExclusivelyPenetrative):
    name = "doggy style"
    url = "https://en.wikipedia.org/wiki/Doggy_style"


class NonExclusivelyPenetrative(Penetrative):
    name = "non exclusively penetrative positions/acts"
    url = ""


class SexualOrientation(PornGenre):
    name = "sexual orientation"
    url = ""


class Bisexual(SexualOrientation):
    name = "bisexual"
    url = "https://en.wikipedia.org/wiki/bisexuality"


class Heterosexual(SexualOrientation):
    name = "heterosexual"
    url = ""


class Homosexual(SexualOrientation):
    name = "homosexual"
    url = ""


class Gay(Homosexual):
    name = "gay"
    url = "https://en.wikipedia.org/wiki/gay"


class Lesbian(Homosexual):
    name = "lesbian"
    url = "https://en.wikipedia.org/wiki/lesbian"


class PornStyle(PornTag):
    name = "pornography style"


class Conventional(PornStyle):
    name = "conventional"


class Gonzo(PornStyle):
    name = "gonzo"


class PornType(PornTag):
    name = "pornography type"


class HardCore(PornType):
    name = "hardcore"


class SoftCore(PornType):
    name = "softcore"


class Place(PornTag):
    name = "place"


class Indoor(Place):
    name = "indoor"


class Outdoor(Place):
    name = "outdoor"
