# -*- coding: utf-8 -*-
"""
city models module.
"""

from sqlalchemy import Unicode, BigInteger

from pyrin.database.model.base import CoreEntity
from pyrin.database.orm.sql.schema.base import CoreColumn
from pyrin.database.orm.sql.schema.columns import AutoPKColumn, FKColumn


class CityBaseEntity(CoreEntity):
    """
    city base entity class.
    """

    _table = 'city'

    id = AutoPKColumn(name='id')


class CityEntity(CityBaseEntity):
    """
    city entity class.
    """

    _extend_existing = True

    name = CoreColumn(name='name', type_=Unicode(200))
    province_id = FKColumn(fk='province.id', name='province_id', type_=BigInteger)
