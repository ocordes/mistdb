"""

storage/metadata.py

written by: Oliver Cordes 2020-07-05
changed by: Oliver Cordes 2020-07-05

"""

import os

import yaml

basefilename = 'metadata.yaml'


class MetaData(object):
    def __init__(self):
        self._data = {}


    def store(self, dirpath):
        filename = os.path.join(dirpath, basefilename)

        with open(filename, 'w') as f:
            data = yaml.dump(self._data, f)


    def load(self, dirpath):
        pass


    def __setitem__(self, key, value):
        self._data[key] = value
