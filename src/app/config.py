"""

app/config.py

written by: Oliver Cordes 2020-07-27
changed by: Oliver Cordes 2020-07-27


"""


import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
