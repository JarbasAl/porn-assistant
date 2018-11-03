from db.pornstars import PornstarDatabase


class PornstarFinder(object):
    """
    """

    def __init__(self, sfw=True, include_amateurs=True):
        """

        Args:
            sfw:
            include_amateurs:
        """
        self.sfw = sfw
        self.db = PornstarDatabase()
        self.include_amateurs = include_amateurs

    def pornstar_in_db(self, name):
        """

        Args:
            name:

        Returns:

        """
        return self.db.is_known(name)

    def search_by_name(self, name):
        """

        Args:
            name:
        """
        pass

    def pornstar_data(self, name):
        """

        Args:
            name:
        """
        pass

    def populate_data(self, name):
        """

        Args:
            name:
        """
        pass
 
