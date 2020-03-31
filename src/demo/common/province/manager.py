# -*- coding: utf-8 -*-
"""
province manager module.
"""

from pyrin.core.structs import Manager
from pyrin.database.services import get_current_store
from pyrin.core.globals import _

from demo.common.province.exceptions import ProvinceNotFoundError
from demo.common.province.models import ProvinceEntity


class ProvinceManager(Manager):
    """
    province manager class.
    """

    def get(self, province_id, **options):
        """
        gets the specified province.

        :param int province_id: province id to get its info.

        :raises ProvinceNotFoundError: province not found error.

        :returns: dict(int id,
                       str name)

        :rtype: dict
        """

        store = get_current_store()
        province = store.query(ProvinceEntity).get(province_id)

        if province is None:
            raise ProvinceNotFoundError(_('Province [{province_id}] not found.'
                                          .format(province_id=province_id)))

        return province.to_dict()

    def find(self, **filters):
        """
        finds provinces with given filters.

        :keyword str name: province name.

        :returns: list[dict(int id,
                            str name)]

        :rtype: list
        """

        clauses = self._make_find_clause(**filters)

        store = get_current_store()
        entities = store.query(ProvinceEntity).filter(*clauses).all()

        return entities

    def get_all(self, **options):
        """
        gets all provinces.

        :returns: list[dict(int id,
                            str name)]

        :rtype: list
        """

        return self.find()

    def _make_find_clause(self, **filters):
        """
        makes the required find clauses based on given
        filters and returns the clauses list.

        :keyword str name: province name.

        :rtype: list
        """

        clauses = []

        name = filters.get('name', None)

        if name is not None:
            clauses.append(ProvinceEntity.name.icontains(name))

        return clauses

    def create(self, name, **options):
        """
        creates a province.

        :param str name: province name.
        """

        province = ProvinceEntity(name=name)
        store = get_current_store()
        store.add(province)
