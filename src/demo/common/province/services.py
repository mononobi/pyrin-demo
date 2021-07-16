# -*- coding: utf-8 -*-
"""
province services module.
"""

from pyrin.application.services import get_component

from demo.common.province import ProvincePackage


def get(id, **options):
    """
    gets the specified province.

    :param int id: province id to get its info.

    :raises ProvinceNotFoundError: province not found error.

    :returns: dict(int id,
                   str name)

    :rtype: ProvinceEntity
    """

    return get_component(ProvincePackage.COMPONENT_NAME).get(id, **options)


def find(**filters):
    """
    finds provinces with given filters.

    :keyword int id: province id.
    :keyword str name: province name.

    :returns: list[dict(int id,
                        str name)]

    :rtype: list
    """

    return get_component(ProvincePackage.COMPONENT_NAME).find(**filters)


def create(name, **options):
    """
    creates a province.

    :param str name: province name.
    """

    return get_component(ProvincePackage.COMPONENT_NAME).create(name, **options)
