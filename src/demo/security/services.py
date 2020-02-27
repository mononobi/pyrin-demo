# -*- coding: utf-8 -*-
"""
security services module.
"""

from pyrin.application.services import get_component

from demo.security import SecurityPackage


def has_permission(user, permissions, **options):
    """
    gets a value indicating that given user has the specified permissions.

    :param user: user identity to check its permissions.
    :param list[PermissionBase] permissions: permissions to check for user.

    :rtype: bool
    """

    return get_component(SecurityPackage.COMPONENT_NAME).has_permission(user,
                                                                        permissions,
                                                                        **options)


def login(username, password, **options):
    """
    logs in the provided user and gets a valid token.

    :param str username: username.
    :param str password: password.

    :raises InvalidUserInfoError: invalid user info error.
    :raises UserNotFoundError: user not found error.
    :raises UserIsNotActiveError: user is not active error.

    :returns: a valid token.
    :rtype: str
    """

    return get_component(SecurityPackage.COMPONENT_NAME).login(username, password, **options)
