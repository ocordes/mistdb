"""

app/demo_routes.py

written by: Oliver Cordes 2020-07-27
changed by: Oliver Cordes 2020-07-27

"""


from flask import Blueprint

bp = Blueprint('demo', __name__)



bp.route('/')
def demo_index():
    return 'Hello, World!'
