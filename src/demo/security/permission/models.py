# -*- coding: utf-8 -*-
"""
permission models module.
"""

from sqlalchemy import Unicode, SmallInteger

from pyrin.database.model.base import CoreEntity
from pyrin.database.orm.sql.schema.columns import AutoPKColumn, StringColumn


class PermissionBaseEntity(CoreEntity):
    """
    permission base entity class.
    """

    _table = 'permission'

    id = AutoPKColumn(type_=SmallInteger, name='id')


class PermissionEntity(PermissionBaseEntity):
    """
    permission entity class.
    """

    _extend_existing = True

    description = StringColumn(name='description', max_length=100, nullable=False, validated=True)
