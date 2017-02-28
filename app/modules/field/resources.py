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
api = Namespace('fields',
                description="Handle fields of your protocol",
                path=projects.path+'/fields')  # pylint: disable=invalid-name


@api.route('/')
class Fields(Resource):

    @api.expect(pagination_parameters, validate = True)
    def get(self, pid):
        """List all fields

        Returns a list of fields starting from ``offset`` limited by ``limit`` parameter.
        """

        args = pagination_parameters.parse_args(request)
        limit = args['limit']
        offset = args['offset']        
        
        project_handler = projects.projects_manager.get_project_handler(pid)        
        return project_handler.get_fields(limit = limit, offset = offset)

    @api.expect(parameters.new_field, validate = True)
    def post(self, pid):
        """Create a new field."""

        args = parameters.new_field.parse_args(request)
        name = args['name']
        did = args['did']
        
        project_handler = projects.projects_manager.get_project_handler(pid)        
        return project_handler.add_field(name = name, did = did)

@api.route('/<string:fid>/')
class FieldByID(Resource):

    def get(self, pid, fid):
        """Fetch a field by its ID"""
        
        project_handler = projects.projects_manager.get_project_handler(pid)        
        return project_handler.get_field(fid = fid)

    def delete(self, pid, fid):
        """Delete a field"""

        project_handler = projects.projects_manager.get_project_handler(pid)        
        return project_handler.delete_field(fid = fid)
