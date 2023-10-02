#!/usr/bin/python
"""The entry point to our flask application"""

import os
from flask import Flask
from models import storage
from api.v1.views import app_views
from flask_cors import CORS

# create the instance
app = Flask(__name__)

# register the blueprint
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown(exception):
    """Destroy current session"""
    storage.close()


if __name__ == '__main__':
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(os.getenv('HBNB_API_PORT', 5000))
    app.run(host=host, port=port, threaded=True)
