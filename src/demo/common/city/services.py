# -*- coding: utf-8 -*-
"""
city services module.
"""

from pyrin.application.services import get_component

from demo.common.city import CityPackage


def get(id, **options):
    """
    gets the specified city.

    :param int id: city id to get its info.

    :raises CityNotFoundError: city not found error.

    :returns: dict(int id,
                   str name,
                   int province_id)

    :rtype: CityEntity
    """

    return get_component(CityPackage.COMPONENT_NAME).get(id, **options)


def find(**filters):
    """
    finds cities with given filters.

    :keyword int id: city id.
    :keyword str name: city name.
    :keyword int province_id: province id.

    :returns: list[dict(int id,
                        str name,
                        int province_id)]

    :rtype: list
    """

    return get_component(CityPackage.COMPONENT_NAME).find(**filters)


def create(name, province_id, **options):
    """
    creates a city.

    :param str name: city name.
    :param int province_id: province id.
    """

    return get_component(CityPackage.COMPONENT_NAME).create(name, province_id, **options)
