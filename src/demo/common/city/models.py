# -*- coding: utf-8 -*-
"""
city models module.
"""

from sqlalchemy import Unicode, Integer, ForeignKey

from pyrin.core.structs import DTO
from pyrin.database.model.base import CoreEntity
from pyrin.database.orm.sql.schema.base import CoreColumn


class CityBaseEntity(CoreEntity):
    """
    city base entity class.
    """

    __tablename__ = 'city'

    id = CoreColumn(name='id', autoincrement=True, type_=Integer, primary_key=True)


class CityEntity(CityBaseEntity):
    """
    city entity class.
    """

    __table_args__ = DTO(extend_existing=True)

    name = CoreColumn(name='name', type_=Unicode)

    province_id = CoreColumn(ForeignKey('province.id'),
                             name='province_id', type_=Integer)
