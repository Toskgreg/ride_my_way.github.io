# -*- coding: utf-8 -*-
"""
Main app root of the api endpoints
"""

import sys
import os
from flask import Flask
from flask_cors import CORS
sys.path.append(os.path.pardir)

from api.config import Config
from api.handlers import ErrorHandlers
from api.views import Urls


class Server(Flask):

    """ Creates flask object to start the server"""

    def __init__(self, *args, **kwargs):
        if not args:
            kwargs.setdefault('import_name', __name__)
        Flask.__init__(self, *args, **kwargs)

        
        
        self.errorhandler(404)(ErrorHandlers.not_found)
        self.errorhandler(400)(ErrorHandlers.bad_request)

        Urls.generate(self)
        CORS(self)


APP = Server()

if __name__ == '__main__':
    APP.run()
