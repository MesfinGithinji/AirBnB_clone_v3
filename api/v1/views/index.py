#!/usr/bin/python
"""Initial routes"""

from flask import jsonify
from api.v1.views import app_views
from models import storage


@app_views.route('/status')
def status_check():
    """Returns OK status code"""
    return jsonify({"status": "OK"})
