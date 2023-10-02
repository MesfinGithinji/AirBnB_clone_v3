#!/usr/bin/python
"""Initial routes"""

from flask import jsonify
from api.v1.views import app_views
from models import storage


@app_views.route('/status')
def status_check():
    """Returns OK status code"""
    return jsonify({"status": "OK"})

@app_views.route('/stats')
def get_stats():
    '''Gets the number of objects for each type.
    '''
    objects = {
        'amenities': Amenity,
        'cities': City,
        'places': Place,
        'reviews': Review,
        'states': State,
        'users': User
    }
    for key, value in objects.items():
        objects[key] = storage.count(value)
    return jsonify(objects)
