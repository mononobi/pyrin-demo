# -*- coding: utf-8 -*-
"""
users api module.
"""

from pyrin.api.router.decorators import post, api

import demo.security.users.services as user_services

from demo.security.users.permissions import VIEW_USERS_LIST_PERMISSION


@post('/users', authenticated=False)
def create(username, password, first_name, last_name, **options):
    """
    creates a new user based on given inputs.
    ---
    parameters:
      - name: username
        type: string
        description: username
      - name: password
        type: string
        format: password
        description: password
      - name: first_name
        type: string
        description: first name
      - name: last_name
        type: string
        description: last name
    """

    user_services.create(username, password, first_name, last_name, **options)


@api('/users/info', permissions=VIEW_USERS_LIST_PERMISSION)
def get_info(**options):
    """
    gets the current user info.
    ---
    responses:
      200:
        description: current user info
        schema:
          properties:
            id:
              type: integer
              description: user id
            username:
              type: string
              description: username
            last_login_date:
              type: string
              format: date-time
              description: last login date
            first_name:
              type: string
              description: first name
            last_name:
              type: string
              description: last name
            is_active:
              type: boolean
              description: user is active
    """

    return user_services.get_info(**options)


@api('/users', authenticated=False, paged=True)
def get_all(**options):
    """
    gets a list of all users.
    ---
    responses:
      200:
        description: list of all users
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
                description: user id
              username:
                type: string
                description: username
              last_login_date:
                type: string
                format: date-time
                description: last login date
              first_name:
                type: string
                description: first name
              last_name:
                type: string
                description: last name
              is_active:
                type: boolean
                description: user is active
    """

    return user_services.get_all(**options)
