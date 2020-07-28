"""

app/demo/__init__.py

written by: Oliver Cordes 2020-07-28
changed by: Oliver Cordes 2020-07-28

"""


from flask import Blueprint

bp = Blueprint('appdemo', __name__)


from app.demo import routes
