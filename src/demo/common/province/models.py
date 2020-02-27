# -*- coding: utf-8 -*-
"""
province models module.
"""

from sqlalchemy import Unicode, Integer

from pyrin.core.context import DTO
from pyrin.database.model.base import CoreEntity
from pyrin.database.orm.sql.schema.base import CoreColumn


class ProvinceBaseEntity(CoreEntity):
    """
    province base entity class.
    """

    __tablename__ = 'province'

    id = CoreColumn(name='id', autoincrement=True, type_=Integer, primary_key=True)


class ProvinceEntity(ProvinceBaseEntity):
    """
    province entity class.
    """

    __table_args__ = DTO(extend_existing=True)

    name = CoreColumn(name='name', type_=Unicode, unique=True)
