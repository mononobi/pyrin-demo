# -*- coding: utf-8 -*-
"""
city api module.
"""

from pyrin.api.router.decorators import api, post

import demo.common.city.services as city_services


@api('/cities/<int:id>', authenticated=False)
def get(id, **options):
    """
    gets the specified city.
    ---
    parameters:
      - name: id
        type: integer
        description: city id to get its info
    responses:
      200:
        description: city info
        schema:
          properties:
            id:
              type: integer
              description: city id
            name:
              type: string
              description: city name
            province_id:
              type: integer
              description: province id
      422:
        description: city not found
    """

    return city_services.get(id, **options)


@api('/cities', authenticated=False)
def find(**filters):
    """
    finds cities with given filters.
    ---
    parameters:
      - name: name
        type: string
        description: city name
      - name: province_id
        type: integer
        description: province id
    responses:
      200:
        description: list of found cities
        schema:
          properties:
            count:
              type: integer
              description: count of found cities
            results:
             type: array
             description: list of found cities
             items:
               type: object
               properties:
                 id:
                   type: integer
                   description: city id
                 name:
                   type: string
                   description: city name
                 province_id:
                   type: integer
                   description: province id
    """

    return city_services.find(**filters)


@post('/cities', authenticated=False)
def create(name, province_id, **options):
    """
    creates a city.
    ---
    parameters:
      - name: name
        type: string
        description: city name
      - name: province_id
        type: integer
        description: province id
    """

    return city_services.create(name, province_id, **options)
