# -*- coding: utf-8 -*-
"""
province api module.
"""

from pyrin.api.router.decorators import api, post

import demo.common.province.services as province_services


@api('/provinces/<int:id>', authenticated=False)
def get(id, **options):
    """
    gets the specified province.
    ---
    parameters:
      - name: id
        type: integer
        description: province id to get its info
    responses:
      200:
        description: province info
        schema:
           properties:
             id:
               type: integer
               description: province id
             name:
               type: string
               description: province name
      422:
        description: province not found
    """

    return province_services.get(id, **options)


@api('/provinces', authenticated=False)
def find(**filters):
    """
    finds provinces with given filters.
    ---
    parameters:
      - name: name
        type: string
        description: province name
    responses:
      200:
        description: list of found provinces
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
                description: province id
              name:
                type: string
                description: province name
    """

    return province_services.find(**filters)


@post('/provinces', authenticated=False)
def create(name, **options):
    """
    creates a province.
    ---
    parameters:
      - name: name
        type: string
        description: province name
    """

    return province_services.create(name, **options)
