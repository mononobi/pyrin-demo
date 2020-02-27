# -*- coding: utf-8 -*-
"""
security exceptions module.
"""

from pyrin.core.exceptions import CoreBusinessException, CoreException
from pyrin.security.authentication.exceptions import AuthenticationFailedError


class SecurityManagerException(CoreException):
    """
    security manager exception.
    """
    pass


class SecurityManagerBusinessException(CoreBusinessException,
                                       SecurityManagerException):
    """
    security manager business exception.
    """
    pass


class InvalidUsernameOrPasswordError(AuthenticationFailedError,
                                     SecurityManagerBusinessException):
    """
    invalid username or password error.
    """
    pass


class UserNotFoundError(AuthenticationFailedError,
                        SecurityManagerBusinessException):
    """
    user not found error.
    """
    pass
