# -*- coding: utf-8 -*-
"""
security models module.
"""

from sqlalchemy import Unicode, DateTime, Boolean

from pyrin.database.model.base import CoreEntity
from pyrin.database.orm.sql.schema.base import CoreColumn
from pyrin.database.orm.sql.schema.columns import AutoPKColumn


class UserBaseEntity(CoreEntity):
    """
    user base entity class.
    """

    _table = 'user'

    id = AutoPKColumn(name='id')


class UserEntity(UserBaseEntity):
    """
    user entity class.
    """

    _extend_existing = True

    username = CoreColumn(name='username', type_=Unicode(50), nullable=False, unique=True)
    password_hash = CoreColumn(name='password_hash', type_=Unicode(250),
                               nullable=False, allow_read=False, allow_write=False)
    last_login_date = CoreColumn(name='last_login_date', type_=DateTime(timezone=True))
    first_name = CoreColumn(name='first_name', type_=Unicode(50), nullable=False)
    last_name = CoreColumn(name='last_name', type_=Unicode(50), nullable=False)
    is_active = CoreColumn(name='is_active', type_=Boolean, nullable=False, default=True)
