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


new_message = reqparse.RequestParser()
new_message.add_argument('cid',
                        type = str,
                        required = True,
                        location = 'json',
                        help = "Capture ID")
new_message.add_argument('data',
                        type = str,
                        required = True,
                        location = 'json',
                        help = "Data transported by the message")
new_message.add_argument('date',
                        type = str,
                        required = False,
                        location = 'json',
                        help = "Message's date")
new_message.add_argument('source',
                        type = str,
                        required = False,
                        location = 'json',
                        help = "Name of the source of the message")
new_message.add_argument('destination',
                        type = str,
                        required = False,
                        location = 'json',
                        help = "Name of the destination of the message")

