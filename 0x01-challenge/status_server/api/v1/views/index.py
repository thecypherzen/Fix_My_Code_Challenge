#!/usr/bin/python3
""" Index view
"""
from flask import json, Response

from api.v1.views import app_views


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """ Status of the web server
    """
    res = json.dumps({"status": "OK"}, indent=2) + '\n'
    return Response(res, mimetype="application/json")
