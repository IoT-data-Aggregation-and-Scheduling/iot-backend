
from flask import Blueprint, Flask, session, redirect, render_template, \
    request, url_for, jsonify, make_response

import requests
import os

mainApp = Blueprint('mainApp', __name__, static_folder='static/')



"""
Add All Routres Here
"""
@anc.route('/', methods=['POST', 'GET'])
def index():
    """
    Main Flask Route
    """
    
    pass