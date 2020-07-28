"""

app/demo_routes.py

written by: Oliver Cordes 2020-07-27
changed by: Oliver Cordes 2020-07-27

"""

from app.demo import bp

print('blubber')

@bp.route('/', methods=['GET'])
def demo_index():
    return 'Hello, World!'


@bp.route('/test', methods=['GET'])
def demo_index2():
    return 'Hello, World!'
