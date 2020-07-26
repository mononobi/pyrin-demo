# -*- coding: utf-8 -*-
"""
city api module.
"""

from pyrin.api.router.decorators import api
from pyrin.core.enumerations import HTTPMethodEnum

import demo.common.city.services as city_services


@api('/cities/<int:city_id>', methods=HTTPMethodEnum.GET, authenticated=False)
def get(city_id, **options):
    """
    gets the specified city.

    :param int city_id: city id to get its info.

    :raises CityNotFoundError: city not found error.

    :returns: dict(int id,
                   str name,
                   int province_id: province id)

    :rtype: dict
    """

    return city_services.get(city_id, **options)


@api('/cities/find', methods=HTTPMethodEnum.GET, authenticated=False)
def find(**filters):
    """
    finds cities with given filters.

    :keyword str name: city name.
    :keyword int province_id: province id.

    :returns: list[dict(int id,
                        str name,
                        int province_id: province id)]

    :rtype: list
    """

    return city_services.find(**filters)


@api('/cities', methods=HTTPMethodEnum.POST, authenticated=False)
def create(name, province_id, **options):
    """
    creates a city.

    :param str name: city name.
    :param int province_id: province id.
    """

    return city_services.create(name, province_id, **options)
