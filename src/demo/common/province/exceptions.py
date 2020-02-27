# -*- coding: utf-8 -*-
"""
province exceptions module.
"""

from pyrin.core.exceptions import CoreException, CoreBusinessException


class ProvinceManagerException(CoreException):
    """
    province manager exception.
    """
    pass


class ProvinceManagerBusinessException(CoreBusinessException,
                                       ProvinceManagerException):
    """
    province manager business exception.
    """
    pass


class ProvinceNotFoundError(ProvinceManagerBusinessException):
    """
    province not found error.
    """
    pass
