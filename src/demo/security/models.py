# -*- coding: utf-8 -*-
"""
security models module.
"""

from sqlalchemy import Unicode, Boolean, TIMESTAMP

from pyrin.database.model.base import CoreEntity
from pyrin.database.orm.sql.schema.base import CoreColumn
from pyrin.database.orm.sql.schema.columns import AutoPKColumn, HiddenColumn, StringColumn


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

    username = StringColumn(name='username', max_length=50,
                            nullable=False, unique=True, validated=True)
    password_hash = HiddenColumn(name='password_hash', type_=Unicode(250), nullable=False)
    last_login_date = CoreColumn(name='last_login_date',
                                 type_=TIMESTAMP(timezone=True), validated=True)
    first_name = StringColumn(name='first_name', max_length=50, nullable=False, validated=True)
    last_name = StringColumn(name='last_name', max_length=50, nullable=False, validated=True)
    is_active = CoreColumn(name='is_active', type_=Boolean, nullable=False,
                           default=True, validated=True)
