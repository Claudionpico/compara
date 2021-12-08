from flask import Response
from flask import Blueprint
import json
from api import app
import requests
from flask import request

from flask import render_template, make_response, url_for
from api.api_0_1.models.car import Car

from functools import wraps
from views import *
from werkzeug.security import check_password_hash

custom_api = Blueprint('custom_api', __name__)
from .exceptions import *

@custom_api.route('/car', methods=['GET'])

def get_car():
    body_pipedrive =''
    pipedrive = PipeDriveApi(app.config['PIPEDRIVE']['host'], app.config['PIPEDRIVE']['token'])

    if data.get('status') is not None:
        body_pipedrive += '&status=' + data.get('status')
    if data.get('limit') is not None:
        body_pipedrive += '&limit=' + data.get('limit')
    if data.get('start') is not None:
        body_pipedrive += '&start=' + data.get('start')
    try:
        list_deals = pipedrive.get('deals', body_pipedrive)
    except:
        raise InternalServerErrorException('Connection Error get deals in PipeDrive ')

    options['body'] = list_deals
    return __build_response_msg(options=options)