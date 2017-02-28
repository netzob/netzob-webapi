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

"""
Projects extension
=============
"""


import logging

from app.extensions.api import api_v1
from app.core.ProjectsManager import ProjectsManager


projects_manager = ProjectsManager()

path = '/p/<string:pid>'

def init_app(app, **kwargs):
    # pylint: disable=unused-argument
    """
    Projects extension initialization point.
    """
    #app.route('/swaggerui/<path:path>')(serve_swaggerui_assets)

