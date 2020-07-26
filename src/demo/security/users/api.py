# -*- coding: utf-8 -*-
"""
users api module.
"""

from pyrin.api.router.decorators import api
from pyrin.core.enumerations import HTTPMethodEnum

import demo.security.users.services as user_services

from demo.security.users.permissions import VIEW_USERS_LIST_PERMISSION


@api('/users', methods=HTTPMethodEnum.POST, authenticated=False)
def create(username, password, first_name, last_name, **options):
    """
    creates a new user based on given inputs.

    :param str username: username.
    :param str password: password.
    :param str first_name: first name.
    :param str last_name: last name.
    """

    user_services.create(username, password, first_name, last_name, **options)


@api('/users/info', methods=HTTPMethodEnum.GET, permissions=VIEW_USERS_LIST_PERMISSION)
def get_info(**options):
    """
    gets the current user info.

    :raises UserNotFoundError: user not found error.

    :returns: dict(int id,
                   str username,
                   datetime last_login_date,
                   str first_name,
                   str last_name,
                   bool is_active)
    :rtype: dict
    """

    return user_services.get(**options)


@api('/users', methods=HTTPMethodEnum.GET, authenticated=False)
def get_all(**options):
    """
    gets a list of all users.

    :returns: list[dict(int id,
                        str username,
                        datetime last_login_date,
                        str first_name,
                        str last_name,
                        bool is_active)]
    :rtype: list
    """

    return user_services.get_all(**options)
