#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# +---------------------------------------------------------------------------+
# | Copyright (C) 2017 Georges Bossert                                        |
# | This program is free software: you can redistribute it and/or modify      |
# | it under the terms of the GNU General Public License as published by      |
# | the Free Software Foundation, either version 3 of the License, or         |
# | (at your option) any later version.                                       |
# |                                                                           |
# | This program is distributed in the hope that it will be useful,           |
# | but WITHOUT ANY WARRANTY; without even the implied warranty of            |
# | MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the              |
# | GNU General Public License for more details.                              |
# |                                                                           |
# | You should have received a copy of the GNU General Public License         |
# | along with this program. If not, see <http://www.gnu.org/licenses/>.      |
# +---------------------------------------------------------------------------+

import logging
import os
import sys
sys.path.insert(0, '.')

from flask import Flask

def configure_app(app):
    # lets set various config values
    app.config['SECRET_KEY'] = "this-really-needs-to-be-changed"
    app.config['URL_PREFIX'] = "/api/v1"
    app.config['DEBUG'] = False
    
    app.config['PROJECT_ROOT'] = os.path.abspath(os.path.dirname(__file__))    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///%s' % (os.path.join(app.config['PROJECT_ROOT'], "netzob-webapi.db"))
    app.config['SWAGGER_UI_JSONEDITOR'] = True
    
    # configure logging
    formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s')
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    handler.setLevel(logging.DEBUG)
    app.logger.addHandler(handler)
    app.logger.setLevel(logging.DEBUG)

def create_app():
    app = Flask(__name__)
    
    configure_app(app)

    import extensions
    extensions.init_app(app)
    
    import modules
    modules.init_app(app)
    
    return app


if __name__ == "__main__":
    
    app = create_app()

    debug_mode = app.config['DEBUG']
    
    app.logger.debug("Web application is ready to start (debug={})".format(debug_mode))
    app.run(debug=debug_mode) 
