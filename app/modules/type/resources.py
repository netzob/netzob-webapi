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
api = Namespace('types',
                description="Handle types of your domains",
                path=projects.path+'/types')  # pylint: disable=invalid-name


@api.route('/')
class Types(Resource):

    @api.expect(pagination_parameters, validate = True)
    def get(self, pid):
        """List all types

        Returns a list of data types starting from ``offset`` limited by ``limit`` parameter.
        """

        args = pagination_parameters.parse_args(request)
        limit = args['limit']
        offset = args['offset']        
        
        project_handler = projects.projects_manager.get_project_handler(pid)        
        return project_handler.get_datatypes(limit = limit, offset = offset)


@api.route('/<string:tid>/')
class TypeByID(Resource):

    def get(self, pid, tid):
        """Fetch a type by its ID"""

        project_handler = projects.projects_manager.get_project_handler(pid)        
        return project_handler.get_datatype(tid = tid)

    def delete(self, pid, tid):
        """Delete a type"""

        project_handler = projects.projects_manager.get_project_handler(pid)        
        return project_handler.delete_datatype(tid = tid)

@api.route('/ascii')
class ASCIITypes(Resource):

    @api.expect(parameters.new_ascii, validate = True)
    def post(self, pid):
        """Create a new ASCII type."""
        
        args = parameters.new_ascii.parse_args(request)
        value = args['value']
        nb_char_min = args['nb_char_min'] 
        nb_char_max = args['nb_char_max']

        project_handler = projects.projects_manager.get_project_handler(pid)        
        return project_handler.create_type_ascii(value = value, nb_char_min = nb_char_min, nb_char_max = nb_char_max)
    
@api.route('/raw')
class RawTypes(Resource):

    @api.expect(parameters.new_raw, validate = True)
    def post(self, pid):
        """Create a new RAW datatype."""
        
        args = parameters.new_raw.parse_args(request)
        value = args['value']
        nb_byte_min = args['nb_byte_min'] 
        nb_byte_max = args['nb_byte_max']

        project_handler = projects.projects_manager.get_project_handler(pid)        
        return project_handler.create_type_raw(value = value, nb_byte_min = nb_byte_min, nb_byte_max = nb_byte_max)
