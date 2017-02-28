# encoding: utf-8
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

from flask_cors import CORS
import logging
logging.getLogger('flask_cors').level = logging.DEBUG
cross_origin_resource_sharing = CORS()

from sqlalchemy_utils import force_auto_coercion, force_instant_defaults
force_auto_coercion()
force_instant_defaults()

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

from . import api
from . import projects

def init_app(app):
    """
    Application extensions initialization.
    """

    EXTENSIONS = (cross_origin_resource_sharing, api, projects, db)

    app.logger.debug("Starts the initializations of extensions.")
    
#        cross_origin_resource_sharing,
#        db,
#        api)

    
    for extension in EXTENSIONS:
        app.logger.error(extension)
        extension.init_app(app)

    app.logger.debug("All the extensions are initialized.")
