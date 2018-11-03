from sqlalchemy.ext.declarative import declarative_base

__author__ = "JarbasAI"


Base = declarative_base()


from sqlalchemy import Column, ForeignKey, Integer, UnicodeText, Unicode, Boolean
from sqlalchemy.orm import relationship
from models.tags import PornGenre


class Pornstar(Base, PornGenre):
    __tablename__ = "stars"
    name = Column(UnicodeText, primary_key=True, nullable=False)

    biography = Column(UnicodeText)
    country = Column(UnicodeText)

    amateur = Column(Boolean, default=False)
    birthday = Column(UnicodeText)

    # body info

    hair_color = Column(UnicodeText)
    ethnicity = Column(Unicode)
    weight = Column(Integer)
    height = Column(Integer)
    cup_size = Column(UnicodeText)
    body_measurements = Column(UnicodeText)

    # computer analysis
    hotness = Column(Integer)

    # user preferences
    sfw_picture = Column(UnicodeText)
    user_rating = Column(Integer)

    # performance data
    blowjob = Column(Boolean)
    facial = Column(Boolean)
    anal = Column(Boolean)
    double_penetration = Column(Boolean)

    # gallery / videos
    media = relationship("PornMedia",
                         back_populates="pornstar",
                         foreign_keys="PornMedia.star",
                         cascade="all, delete-orphan")

    # external db ids
    adam_eve_id = Column(UnicodeText)  # https://www.adamevevod.com/s/porn-stars/ps/179323/adria-rae
    afdb_id = Column(UnicodeText)  # http://www.adultfilmdatabase.com/actor/adria-rae-69117/
    barelist_id = Column(UnicodeText) # http://www.barelist.com/models/id_13685_Adria_Rae.html
    egafd_id = Column(UnicodeText)
    freeones_id = Column(UnicodeText) # https://www.freeones.com/html/a_links/Adria_Rae/
    iafdb_id = Column(UnicodeText) # http://www.iafd.com/person.rme/perfid=adriarae/gender=f/adria-rae.htm
    sweetpornstars_id = Column(UnicodeText) #https://sweet-pornstars.com/adria-rae/
    pornhub_id = Column(UnicodeText) #https://www.pornhub.com/pornstar/adria-rae

    # social media
    twitter = Column(UnicodeText)
    instagram = Column(UnicodeText)
    facebook = Column(UnicodeText)

    def __repr__(self):
        return self.name


class PornMedia(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True, nullable=False)
    url = Column(Unicode)
    type = Column(Unicode, default="picture")
    star = Column(Integer, ForeignKey('stars.name'))
    tags = Column(Unicode, default="adult, xxx")
    pornstar = relationship("Pornstar",
                            back_populates="media")

    def __repr__(self):
        return self.url


def model_to_dict(obj):
    serialized_data = {c.key: getattr(obj, c.key) for c in obj.__table__.columns}
    return serialized_data


def props(cls):
    return [i for i in list(cls.__dict__.keys()) if i[:1] != '_']


