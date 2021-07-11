# -*- coding: utf-8 -*-
"""
security api module.
"""

from pyrin.api.router.decorators import post

import demo.security.services as security_services


@post('/auth/login', authenticated=False)
def login(username, password, **options):
    """
    logs in the provided user and gets a valid access and refresh token.
    ---
    parameters:
      - name: username
        type: string
        description: username
      - name: password
        type: string
        format: password
        description: password
    responses:
      201:
        description: user has successfully logged in
        schema:
          properties:
            access_token:
              type: string
              description: access token
            refresh_token:
              type: string
              description: refresh token
      401:
        description: authentication failed
      403:
        description: user is not active
    """

    return security_services.login(username, password, **options)
