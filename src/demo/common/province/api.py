# -*- coding: utf-8 -*-
"""
province api module.
"""

from pyrin.api.router.decorators import api
from pyrin.core.enumerations import HTTPMethodEnum

import demo.common.province.services as province_services


@api('/provinces/<int:province_id>', methods=HTTPMethodEnum.GET, authenticated=False)
def get(province_id, **options):
    """
    gets the specified province.

    :param int province_id: province id to get its info.

    :raises ProvinceNotFoundError: province not found error.

    :returns: dict(int id,
                   str name)

    :rtype: dict
    """

    return province_services.get(province_id, **options)


@api('/provinces/find', methods=HTTPMethodEnum.GET, authenticated=False)
def find(**filters):
    """
    finds provinces with given filters.

    :keyword str name: province name.

    :returns: list[dict(int id,
                        str name)]

    :rtype: list
    """

    return province_services.find(**filters)


@api('/provinces', methods=HTTPMethodEnum.GET, authenticated=False)
def get_all(**options):
    """
    gets all provinces.

    :returns: list[dict(int id,
                        str name)]

    :rtype: list
    """

    return province_services.get_all(**options)


@api('/provinces', methods=HTTPMethodEnum.POST, authenticated=False)
def create(name, **options):
    """
    creates a province.

    :param str name: province name.
    """

    return province_services.create(name, **options)
