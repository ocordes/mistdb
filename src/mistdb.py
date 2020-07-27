"""

mistdb.py

written by: Oliver Cordes 2020-07-27
changed by: Oliver Cordes 2020-07-27

"""


__author__  = 'Oliver Cordes'
__version__ = '0.0.1'


from app import create_app


# load extra local variables from .env in the local directory
from dotenv import load_dotenv
load_dotenv()


# create an application
application = create_app()
app = application.app


# test this file
if __name__ == "__main__":
    app.run(
    ##socketio.run(app,
            host='0.0.0.0',
            port=4555,
            debug=True,
            extra_files=['./app/api/openapi.yaml'])
    #app.run(port=4555)
