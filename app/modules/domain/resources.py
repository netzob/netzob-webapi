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
api = Namespace('domains',
                description="Handle definition domains of your fields",
                path=projects.path+'/domains')  # pylint: disable=invalid-name


@api.route('/')
class Domains(Resource):

    @api.expect(pagination_parameters, validate = True)
    def get(self, pid):
        """List all domains

        Returns a list of domains starting from ``offset`` limited by ``limit`` parameter.
        """
        args = pagination_parameters.parse_args(request)
        limit = args['limit']
        offset = args['offset']        
        
        project_handler = projects.projects_manager.get_project_handler(pid)        
        return project_handler.get_domains(limit = limit, offset = offset)

@api.route('/<string:did>/')
class DomainByID(Resource):

    def get(self, pid, did):
        """Fetch a domain by its ID"""
        project_handler = projects.projects_manager.get_project_handler(pid)        
        return project_handler.get_domain(did = did)

    def delete(self, pid, did):
        """Delete a domain by its ID"""

        project_handler = projects.projects_manager.get_project_handler(pid)        
        return project_handler.delete_domain(did = did)

@api.route('/data')
class DataDomains(Resource):

    @api.expect(parameters.new_domain_data, vamidate = True)
    def post(self, pid):
        """Create a new data domain"""

        args = parameters.new_domain_data.parse_args(request)
        name = args['name']
        tid = args['tid']
        
        project_handler = projects.projects_manager.get_project_handler(pid)        
        return project_handler.create_domain_data(name = name, tid = tid)

@api.route('/aggregate')
class AggregateDomains(Resource):

    def post(self, pid):
        """Create a new aggregate domain"""

        project_handler = projects.projects_manager.get_project_handler(pid)        
        return project_handler.create_domain_aggregate()

@api.route('/aggregate/<string:aid>')
class ChildrenAggregateDomains(Resource):

    @api.expect(pagination_parameters, validate = True)
    def get(self, pid, aid):
        """Fetches aggregate child domain by ID"""

        args = pagination_parameters.parse_args(request)
        limit = args['limit']
        offset = args['offset']        
        
        project_handler = projects.projects_manager.get_project_handler(pid)        
        return project_handler.get_domains_in_aggregate(aid = aid, limit = limit, offset = offset)

@api.route('/aggregate/<string:aid>/domain/<string:did>')
class ChildAggregateDomains(Resource):

    def delete(self, pid, aid, did):
        """Deletes aggregate child domain by ID"""

        project_handler = projects.projects_manager.get_project_handler(pid)        
        return project_handler.remove_domain_in_aggregate(aid = aid, did = did)

    def put(self, pid, aid, did):
        """Append a new child domain"""

        project_handler = projects.projects_manager.get_project_handler(pid)        
        return project_handler.add_domain_in_aggregate(aid = aid, did = did)
    
    
