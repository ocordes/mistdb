"""

app/demo_routes.py

written by: Oliver Cordes 2020-07-27
changed by: Oliver Cordes 2020-07-27

"""

from app.demo import bp

from flask import current_app, request, render_template, url_for, flash,  \
                  redirect, send_from_directory, jsonify, session


@bp.route('/', methods=['GET'])
@bp.route('/index.html', methods=['GET'])
def demo_index():
    #print(render_template('index.html'))
    return render_template('index.html')


@bp.route('/test', methods=['GET'])
def demo_index2():
    return 'Hello, World!'
