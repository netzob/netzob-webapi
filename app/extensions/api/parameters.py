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

from flask_restplus import reqparse

pagination_parameters = reqparse.RequestParser()
pagination_parameters.add_argument('limit',
                        type=int,
                        required=False,
                        default=20,
                        help="limit a number of items (allowed range is 1-100), default is 20.")

pagination_parameters.add_argument('offset',
                        type=int,
                        required=False,
                        default=0,
                        help="a number of items to skip, default is 0.")
