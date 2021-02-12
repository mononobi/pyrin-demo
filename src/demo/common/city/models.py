# -*- coding: utf-8 -*-
"""
city models module.
"""

from sqlalchemy import Unicode, Integer, ForeignKey

from pyrin.database.model.base import CoreEntity
from pyrin.database.orm.sql.schema.base import CoreColumn
from pyrin.database.orm.sql.schema.columns import PKColumn


class CityBaseEntity(CoreEntity):
    """
    city base entity class.
    """

    _table = 'city'

    id = PKColumn(name='id', type_=Integer, autoincrement=True)


class CityEntity(CityBaseEntity):
    """
    city entity class.
    """

    _extend_existing = True

    name = CoreColumn(name='name', type_=Unicode(200))
    province_id = CoreColumn(ForeignKey('province.id'), name='province_id', type_=Integer)
