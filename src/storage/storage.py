"""

storage/storage.py

written by: Oliver Cordes 2020-06-28
changed by: Oliver Cordes 2020-07-05

"""

import uuid

import os
import hashlib

from .metadata import MetaData

datadir = 'data/'

class Storage(object):
    def __init__(self, id=None):
        self.__id   = id
        self.__meta = None


    def create_directory(self, id):
        """
        create the directory for the data struture
        """
        # choose the first time field as a subdirectory,
        # maybe not the wisest thing ...
        subdir = f'{id.fields[0]:x}'
        dirpath = os.path.join(datadir, subdir, str(id))

        try:
            os.makedirs(dirpath, exist_ok=False)
            return dirpath
        except:
            return None


    def copy_file(self, filename, dirpath, filebase):
        outfilename = os.path.join(dirpath, filebase)

        try:
            outf = open(outfilename, 'wb')
            inf  = open(filename, 'rb')

            md5 = hashlib.md5()
            block_size = 128  # useful size of chunks for md5 hashing
            size = 0

            while True:
                data = inf.read(block_size)
                if not data:
                    break

                md5.update(data)
                outf.write(data)
                size += len(data)

            inf.close()
            outf.close()
        except:
            # whatever happens return a non result
            return None, None

        return md5.hexdigest(), size





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

        # extract the filename base
        filebase = os.path.basename(filename)

        # generate uuid for the new object, cannot be the same,
        # but anyway set 3 attempts to create a new uuid
        retries = 3
        ok = False
        while not ok:
            self.__id = uuid.uuid1()
            dirpath = self.create_directory(self.__id)
            ok = dirpath is not None
            retries -= 1
        if not ok:
            return -1

        # id is now the object id forever

        # store the file into directory return the md5 hash

        md5sum, size = self.copy_file(filename, dirpath, filebase)

        self.__meta = MetaData()
        self.__meta['uuid'] = str(self.__id)
        self.__meta['filebase'] = filebase
        self.__meta['md5sum'] = md5sum
        self.__meta['size'] = size
        self.__meta['encryption'] = False
        self.__meta['author'] = user.username

        self.__meta.store(dirpath)

        return self.__id
