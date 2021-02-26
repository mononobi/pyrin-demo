# -*- coding: utf-8 -*-
"""
city models module.
"""

from sqlalchemy import BigInteger

from pyrin.database.model.base import CoreEntity
from pyrin.database.orm.sql.schema.columns import AutoPKColumn, FKColumn, StringColumn


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

    name = StringColumn(name='name', max_length=50, validated=True)
    province_id = FKColumn(fk='province.id', name='province_id', type_=BigInteger, validated=True)
