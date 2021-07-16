# -*- coding: utf-8 -*-
"""
security models module.
"""

from sqlalchemy import Unicode

from pyrin.database.model.declarative import CoreEntity
from pyrin.database.orm.sql.schema.columns import AutoPKColumn, HiddenColumn, \
    StringColumn, TimeStampColumn, BooleanColumn


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

    username = StringColumn(name='username', max_length=50, min_length=6,
                            nullable=False, unique=True)
    password_hash = HiddenColumn(name='password_hash', type_=Unicode(250), nullable=False)
    last_login_date = TimeStampColumn(name='last_login_date', allow_write=False)
    first_name = StringColumn(name='first_name', max_length=50, nullable=False)
    last_name = StringColumn(name='last_name', max_length=50, nullable=False)
    is_active = BooleanColumn(name='is_active', nullable=False, default=True, allow_write=False)
