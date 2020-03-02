from flask import Blueprint, jsonify
from api import data

api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/about')
def about():
    return jsonify(data.about)

@api.route('/projects')
def projects():
    return jsonify(data.projects)

@api.route('/interests')
def interests():
    return jsonify(data.interests)
