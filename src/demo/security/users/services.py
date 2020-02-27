# -*- coding: utf-8 -*-
"""
users services module.
"""

from pyrin.application.services import get_component

from demo.security.users import UsersPackage


def create(username, password, first_name, last_name, **options):
    """
    creates a new user based on given inputs.

    :param str username: username.
    :param str password: password.
    :param str first_name: first name.
    :param str last_name: last name.
    """

    get_component(UsersPackage.COMPONENT_NAME).create(username, password, first_name,
                                                      last_name, **options)


def get(**options):
    """
    gets the current user info.

    :raises UserNotFoundError: user not found error.

    :rtype: UserEntity
    """

    return get_component(UsersPackage.COMPONENT_NAME).get(**options)


def get_all(**options):
    """
    gets a list of all users.

    :returns: list[UserEntity]
    :rtype: list
    """

    return get_component(UsersPackage.COMPONENT_NAME).get_all(**options)
