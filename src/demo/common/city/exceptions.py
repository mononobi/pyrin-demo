# -*- coding: utf-8 -*-
"""
city exceptions module.
"""

from pyrin.core.exceptions import CoreException, CoreBusinessException


class CityManagerException(CoreException):
    """
    city manager exception.
    """
    pass


class CityManagerBusinessException(CoreBusinessException,
                                   CityManagerException):
    """
    city manager business exception.
    """
    pass


class CityNotFoundError(CityManagerBusinessException):
    """
    city not found error.
    """
    pass
