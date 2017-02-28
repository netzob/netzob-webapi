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


ENABLED_MODULES = [ "symbol", "message", "field", "domain", "type", "capture", "api"]

def init_app(app, **kwargs):
    from importlib import import_module

    app.logger.debug("Starts the initializations of all the modules.")


    for module_name in ENABLED_MODULES:
        import_module('.%s' % module_name, package=__name__).init_app(app, **kwargs)

    app.logger.debug("All the modules are initialized.")
