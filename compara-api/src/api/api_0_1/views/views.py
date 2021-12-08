from functools import wraps
from flask import request
from flask_restless import ProcessingException
from flask import current_app
from api import app
from api.api_0_1.models.model import db
from api.api_0_1.models.car import Car
from api.api_0_1.models.user import User

class Views(object):
    """
    Views
    **Overview**

    Used to generalize attributes and methods for all views package.
    Properties needed to create an endpoint using restless-extension
    """

    preprocessors = None
    postprocessors = None
    url_prefix = '/0.1'
    methods = ['GET', 'POST', 'PATCH','DELETE']
    include_columns = None
    exclude_columns = None


    def __init__(self):
        self.preprocessors = {
            'GET_SINGLE': [self.get_single_preprocessor],
            'GET_MANY': [self.get_many_preprocessor],
            'POST': [self.post_preprocessor],
            'PATCH_SINGLE': [self.patch_single_preprocessor],
            'PATCH_MANY': [self.patch_many_preprocessor],
            'DELETE_SINGLE': [self.delete_single_preprocessor],
            'DELETE_MANY': [self.delete_many_preprocessor]
        }

        self.postprocessors = {
            'GET_SINGLE': [self.get_single_postprocessor],
            'GET_MANY': [self.get_many_postprocessor],
            'POST': [self.post_postprocessor],
            'PATCH_SINGLE': [self.patch_single_postprocessor],
            'PATCH_MANY': [self.patch_many_postprocessor],
            'DELETE_SINGLE': [self.delete_postprocessor],
            'DELETE_MANY': [self.delete_many_postprocessor]
        }


    # Preprocessors
    @staticmethod
    ##@requires_auth
    def get_single_preprocessor(instance_id=None, **kw): pass

    @staticmethod
    #@requires_auth
    def get_many_preprocessor(search_params=None, **kw): pass

    @staticmethod
    #@requires_auth
    def post_preprocessor(data=None, **kw): pass

    @staticmethod
    #@requires_auth
    def patch_single_preprocessor(instance_id=None, data=None, **kw): pass

    @staticmethod
    #@requires_auth
    def patch_many_preprocessor(search_params=None, data=None, **kw): pass

    @staticmethod
    #@requires_auth
    def delete_single_preprocessor(instance_id=None, **kw): pass

    @staticmethod
    #@requires_auth
    def delete_many_preprocessor(search_params=None, **kw): pass


    # Postprocessors
    @staticmethod
    def get_single_postprocessor(result=None, **kw): pass
    @staticmethod
    def get_many_postprocessor(result=None, search_params=None, **kw): pass
    @staticmethod
    def post_postprocessor(result=None, **kw): pass
    @staticmethod
    def patch_single_postprocessor(result=None, **kw): pass
    @staticmethod
    def patch_many_postprocessor(query=None, data=None, search_params=None, **kw): pass
    @staticmethod
    def delete_postprocessor(was_deleted=None, **kw): pass
    @staticmethod
    def delete_many_postprocessor(result=None, search_params=None, **kw): pass
