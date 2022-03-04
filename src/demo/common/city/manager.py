# -*- coding: utf-8 -*-
"""
city manager module.
"""

import pyrin.validator.services as validator_services
import pyrin.filtering.services as filtering_services

from pyrin.core.globals import _
from pyrin.core.structs import Manager
from pyrin.database.services import get_current_store

from demo.common.city.exceptions import CityNotFoundError
from demo.common.city.models import CityEntity


class CityManager(Manager):
    """
    city manager class.
    """

    def get(self, id, **options):
        """
        gets the specified city.

        :param int id: city id to get its info.

        :raises CityNotFoundError: city not found error.

        :returns: dict(int id,
                       str name,
                       int province_id)

        :rtype: CityEntity
        """

        data = validator_services.validate(CityEntity, id=id)
        store = get_current_store()
        city = store.query(CityEntity).get(data.get(id))

        if city is None:
            raise CityNotFoundError(_('City [{city_id}] not found.'
                                      .format(city_id=data.get(id))))

        return city

    def find(self, **filters):
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

        validator_services.validate_for_find(CityEntity, filters)
        clauses = filtering_services.filter(CityEntity, filters)
        store = get_current_store()
        entities = store.query(CityEntity).filter(*clauses).all()
        return entities

    def create(self, name, province_id, **options):
        """
        creates a city.

        :param str name: city name.
        :param int province_id: province id.
        """

        data = dict(name=name, province_id=province_id)
        validator_services.validate_dict(CityEntity, data)
        city = CityEntity(**data)
        store = get_current_store()
        store.add(city)
