# -*- coding: utf-8 -*-
"""
province models module.
"""

from pyrin.database.model.declarative import CoreEntity
from pyrin.database.orm.sql.schema.columns import AutoPKColumn, StringColumn


class ProvinceBaseEntity(CoreEntity):
    """
    province base entity class.
    """

    _table = 'province'

    id = AutoPKColumn(name='id')


class ProvinceEntity(ProvinceBaseEntity):
    """
    province entity class.
    """

    _extend_existing = True

    name = StringColumn(name='name', max_length=200, unique=True)
