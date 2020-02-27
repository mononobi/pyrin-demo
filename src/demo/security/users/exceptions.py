# -*- coding: utf-8 -*-
"""
users exceptions module.
"""

from pyrin.core.exceptions import CoreBusinessException, CoreException


class UsersManagerException(CoreException):
    """
    users manager exception.
    """
    pass


class UsersManagerBusinessException(CoreBusinessException,
                                    UsersManagerException):
    """
    users manager business exception.
    """
    pass


class InvalidUserIDError(UsersManagerBusinessException):
    """
    invalid user id error.
    """
    pass
