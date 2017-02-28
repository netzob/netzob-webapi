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

import logging

from flask import request
from flask_restplus import Namespace, Resource, fields
from app.extensions.api.parameters import pagination_parameters
from app.extensions import projects

from . import parameters


log = logging.getLogger(__name__)  # pylint: disable=invalid-name
api = Namespace('users',
                description="",
                path='/users')  # pylint: disable=invalid-name


@api.route('/')
class User(Resource):

    @api.expect(pagination_parameters, validate = True)
    def get(self):
        """List all users

        Returns a list of users starting from ``offset`` limited by ``limit`` parameter.
        """

        args = pagination_parameters.parse_args(request)
        limit = args['limit']
        offset = args['offset']        
        
