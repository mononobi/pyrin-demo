# -*- coding: utf-8 -*-
"""
city manager module.
"""

from pyrin.core.structs import Manager
from pyrin.database.services import get_current_store
from pyrin.core.globals import _

from demo.common.city.exceptions import CityNotFoundError
from demo.common.city.models import CityEntity


class CityManager(Manager):
    """
    city manager class.
    """

    def get(self, city_id, **options):
        """
        gets the specified city.

        :param int city_id: city id to get its info.

        :raises CityNotFoundError: city not found error.

        :returns: dict(int id,
                       str name,
                       int province_id: province id)

        :rtype: dict
        """

        store = get_current_store()
        city = store.query(CityEntity).get(city_id)

        if city is None:
            raise CityNotFoundError(_('City [{city_id}] not found.'
                                      .format(city_id=city_id)))

        return city.to_dict()

    def find(self, **filters):
        """
        finds cities with given filters.

        :keyword str name: city name.
        :keyword int province_id: province id.

        :returns: list[dict(int id,
                            str name,
                            int province_id: province id)]

        :rtype: list
        """

        clauses = self._make_find_clause(**filters)

        store = get_current_store()
        entities = store.query(CityEntity).filter(*clauses).all()

        return entities

    def _make_find_clause(self, **filters):
        """
        makes the required find clauses based on
        given filters and returns the clauses list.

        :keyword str name: city name.
        :keyword int province_id: province id.

        :rtype: list
        """

        clauses = []

        name = filters.get('name', None)
        province_id = filters.get('province_id', None)

        if name is not None:
            clauses.append(CityEntity.name.icontains(name))

        if province_id is not None:
            clauses.append(CityEntity.province_id == province_id)

        return clauses

    def create(self, name, province_id, **options):
        """
        creates a city.

        :param str name: city name.
        :param int province_id: province id.
        """

        city = CityEntity(name=name, province_id=province_id)
        store = get_current_store()
        store.add(city)
