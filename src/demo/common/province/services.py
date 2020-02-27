# -*- coding: utf-8 -*-
"""
province services module.
"""

from pyrin.application.services import get_component

from demo.common.province import ProvincePackage


def get(province_id, **options):
    """
    gets the specified province.

    :param int province_id: province id to get its info.

    :raises ProvinceNotFoundError: province not found error.

    :returns: dict(int id,
                   str name)

    :rtype: dict
    """

    return get_component(ProvincePackage.COMPONENT_NAME).get(province_id, **options)


def find(**filters):
    """
    finds provinces with given filters.

    :keyword str name: province name.

    :returns: list[dict(int id,
                        str name)]

    :rtype: list
    """

    return get_component(ProvincePackage.COMPONENT_NAME).find(**filters)


def get_all(**options):
    """
    gets all provinces.

    :returns: list[dict(int id,
                        str name)]

    :rtype: list
    """

    return get_component(ProvincePackage.COMPONENT_NAME).get_all(**options)


def create(name, **options):
    """
    creates a province.

    :param str name: province name.
    """

    return get_component(ProvincePackage.COMPONENT_NAME).create(name, **options)
