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


new_capture = reqparse.RequestParser()
new_capture.add_argument('name',
                        type = str,
                        required = True,
                        location = 'json',
                        help = "Name of the capture")
new_capture.add_argument('date',
                        type = str,
                        required = False,
                        location = 'json',
                        help = "Capture's date")

