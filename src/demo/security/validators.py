# -*- coding: utf-8 -*-
"""
security validators module.
"""

from pyrin.validator.decorators import validator
from pyrin.validator.handlers.string import StringValidator

from demo.security.models import UserEntity


@validator(UserEntity, UserEntity.password_hash, name='password')
class PasswordValidator(StringValidator):
    """
    password validator class.
    """

    default_minimum_length = 4
    default_maximum_length = 20
