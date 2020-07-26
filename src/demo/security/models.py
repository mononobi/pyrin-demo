# -*- coding: utf-8 -*-
"""
security models module.
"""

from sqlalchemy import Unicode, DateTime, Integer, Boolean

from pyrin.core.structs import DTO
from pyrin.database.model.base import CoreEntity
from pyrin.database.orm.sql.schema.base import CoreColumn


class UserBaseEntity(CoreEntity):
    """
    user base entity class.
    """

    __tablename__ = 'user'

    id = CoreColumn(name='id', type_=Integer, autoincrement=True,
                    primary_key=True, index=True)


class UserEntity(UserBaseEntity):
    """
    user entity class.
    """

    __table_args__ = DTO(extend_existing=True)

    username = CoreColumn(name='username', type_=Unicode(50), nullable=False, unique=True)
    password_hash = CoreColumn(name='password_hash', type_=Unicode(250),
                               nullable=False, exposed=False)
    last_login_date = CoreColumn(name='last_login_date', type_=DateTime(timezone=True))
    first_name = CoreColumn(name='first_name', type_=Unicode(50), nullable=False)
    last_name = CoreColumn(name='last_name', type_=Unicode(50), nullable=False)
    is_active = CoreColumn(name='is_active', type_=Boolean, nullable=False, default=True)
