# -*- coding: utf-8 -*-
"""
city api module.
"""

from pyrin.api.router.decorators import api
from pyrin.core.enumerations import HTTPMethodEnum

import demo.common.city.services as city_services


@api('/common/city/get/<int:city_id>', methods=HTTPMethodEnum.GET, login_required=False)
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


@api('/common/city/find', methods=HTTPMethodEnum.GET, login_required=False)
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


@api('/common/city/create', methods=HTTPMethodEnum.POST, login_required=False)
def create(name, province_id, **options):
    """
    creates a city.

    :param str name: city name.
    :param int province_id: province id.
    """

    return city_services.create(name, province_id, **options)
