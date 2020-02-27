# -*- coding: utf-8 -*-
"""
security api module.
"""

from pyrin.api.router.decorators import api
from pyrin.core.enumerations import HTTPMethodEnum

import demo.security.services as security_services


@api('/security/login', methods=HTTPMethodEnum.POST, login_required=False)
def login(username, password, **options):
    """
    logs in the provided user and gets a valid token.

    :param str username: username.
    :param str password: password.

    :returns: a valid token.
    :rtype: str
    """

    return security_services.login(username, password, **options)
