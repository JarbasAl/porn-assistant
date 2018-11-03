from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError

from models import Base, Pornstar, PornMedia

from os.path import join, expanduser

from settings import DATABASE_DIR


class PornstarDatabase(object):
    def __init__(self, debug=False):
        path = 'favorite_stars.db'
        self.path = "sqlite:///" + join(DATABASE_DIR, path)
        self.db = create_engine(self.path)
        Base.metadata.create_all(self.db)
        self.db.echo = debug
        Session = sessionmaker(bind=self.db)
        self.session = Session()

    def is_known(self, name):
        entry = self.first_result(name)
        if not entry:
            return False
        return True

    def get_stars(self):
        return self.session.query(Pornstar).all()

    def search_amateur(self, type):
        return self.session.query(Pornstar).filter_by(amateur=True).all()

    def search(self, name, no_amateur=True):
        if no_amateur:
            return self.session.query(Pornstar).filter_by(name=name, amateur=False).all()
        return self.session.query(Pornstar).filter_by(name=name).all()

    def first_result(self, name):
        return self.session.query(Pornstar).filter_by(name=name).first()

    def add_star(self, name=None, amateur=False):
        entry = self.first_result(name)
        if not entry:
            star = Pornstar(name=name, amateur=amateur)
            self.session.add(star)
            if self.commit():
                return star
        return None

    def total_stars(self):
        return self.session.query(Pornstar).count()

    def commit(self):
        try:
            self.session.commit()
            return True
        except IntegrityError:
            self.session.rollback()
            return False
