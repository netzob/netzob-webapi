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


from sqlalchemy_utils import types as column_types, Timestamp
from app.extensions import db

class User(db.Model, Timestamp):
    """
    User database model
    """

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(length=80), unique=True, nullable=False)
    password = db.Column(
        column_types.PasswordType(
            max_length=128,
            schemes=('bcrypt', )
        ),
        nullable=False
    )
    email = db.Column(db.String(length=120), unique=True, nullable=False)
    first_name = db.Column(db.String(length=30), default='', nullable=False)
    last_name = db.Column(db.String(length=30), default='', nullable=False)

    @classmethod
    def find_with_password(cls, username, password):
        """
        Args:
            username (str)
            password (str) - plain-text password
        Returns:
            user (User) - if there is a user with a specified username and
            password, None otherwise.
        """
        user = cls.query.filter_by(username=username).first()
        if not user:
            return None
        if user.password == password:
            return user
        return None

    
