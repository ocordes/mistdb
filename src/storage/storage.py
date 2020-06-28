"""

storage/storage.py

written by: Oliver Cordes 2020-06-28
changed by: Oliver Cordes 2020-06-28

"""

import uuid

import os


class Storage(object):
    def __init__(self, id=None):
        self.__id = id


    def create_directory(self, id):
        return 0


    def push(self, filename, user):
        """
        push

        Parameters
        ----------
        filename:
            the name of the file to add into the Storage
        user:
            the user object with the information what to do,
            access rights, encryption etc.

        returns:
            the id of the new object
        """

        # generate uuid for the new object, cannot be the same
        id = uuid.uuid1()

        
        ret = self.create_directory(id)

        return id
