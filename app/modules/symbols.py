import logging

from flask_restplus import Namespace, Resource, fields

from core.Project import Project
from core.parameters import pagination_parameters
from .symbols_parameters import symbol_parameters

api = Namespace('symbol', description='Symbol related operations')

symbol = api.model('Symbol', {
    'name': fields.String(required=True, description='The name of the symbol'),
})

def get_current_project():
    return "test"

@api.route('/')
class SymbolList(Resource):
    
    @api.doc('list_symbols')
    @api.expect(pagination_parameters())
    @api.marshal_list_with(symbol)
    def get(self):
        '''List all symbols of a project'''
        project = Project.get_project_by_name(get_current_project)        
        return project.protocol.vocabulary.symbols

    @api.doc('create_symbol')
    @api.expect(symbol_parameters())
    @api.marshal_with(symbol, code=201)
    def post(self):
        
        project = Project.get_project_by_name(get_current_project)

        logging.info("PAN: {}".format(**args))
        
        return 201

@api.route('/<id>')
@api.param('id', 'The symbol identifier')
@api.response(404, 'Symbol not found')
class Symbol(Resource):
    @api.doc('get_symbol')
    @api.marshal_with(symbol)
    def get(self, id):
        '''Fetch a symbol given its identifier'''

        
        
        api.abort(404)
