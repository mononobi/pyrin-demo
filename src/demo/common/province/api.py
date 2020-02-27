# -*- coding: utf-8 -*-
"""
province api module.
"""

from pyrin.api.router.decorators import api
from pyrin.core.enumerations import HTTPMethodEnum

import demo.common.province.services as province_services


@api('/common/province/get/<int:province_id>', methods=HTTPMethodEnum.GET, login_required=False)
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


@api('/common/province/find', methods=HTTPMethodEnum.GET, login_required=False)
def find(**filters):
    """
    finds provinces with given filters.

    :keyword str name: province name.

    :returns: list[dict(int id,
                        str name)]

    :rtype: list
    """

    return province_services.find(**filters)


@api('/common/province/get_all', methods=HTTPMethodEnum.GET, login_required=False)
def get_all(**options):
    """
    gets all provinces.

    :returns: list[dict(int id,
                        str name)]

    :rtype: list
    """

    return province_services.get_all(**options)


@api('/common/province/create', methods=HTTPMethodEnum.POST, login_required=False)
def create(name, **options):
    """
    creates a province.

    :param str name: province name.
    """

    return province_services.create(name, **options)
