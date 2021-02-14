# -*- coding: utf-8 -*-
"""
province models module.
"""

from sqlalchemy import Unicode

from pyrin.database.model.base import CoreEntity
from pyrin.database.orm.sql.schema.base import CoreColumn
from pyrin.database.orm.sql.schema.columns import AutoPKColumn


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

    name = CoreColumn(name='name', type_=Unicode(200), unique=True)
