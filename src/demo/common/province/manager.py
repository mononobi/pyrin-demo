# -*- coding: utf-8 -*-
"""
province manager module.
"""

import pyrin.validator.services as validator_services
import pyrin.filtering.services as filtering_services

from pyrin.core.globals import _
from pyrin.core.structs import Manager
from pyrin.database.services import get_current_store

from demo.common.province.exceptions import ProvinceNotFoundError
from demo.common.province.models import ProvinceEntity


class ProvinceManager(Manager):
    """
    province manager class.
    """

    def get(self, id, **options):
        """
        gets the specified province.

        :param int id: province id to get its info.

        :raises ProvinceNotFoundError: province not found error.

        :returns: dict(int id,
                       str name)

        :rtype: ProvinceEntity
        """

        data = validator_services.validate(ProvinceEntity, id=id)
        store = get_current_store()
        province = store.query(ProvinceEntity).get(data.id)

        if province is None:
            raise ProvinceNotFoundError(_('Province [{province_id}] not found.'
                                          .format(province_id=data.id)))

        return province

    def find(self, **filters):
        """
        finds provinces with given filters.

        :keyword int id: province id.
        :keyword str name: province name.

        :returns: list[dict(int id,
                            str name)]

        :rtype: list
        """

        validator_services.validate_for_find(ProvinceEntity, filters)
        clauses = filtering_services.filter(ProvinceEntity, filters)
        store = get_current_store()
        entities = store.query(ProvinceEntity).filter(*clauses).all()
        return entities

    def create(self, name, **options):
        """
        creates a province.

        :param str name: province name.
        """

        name = validator_services.validate_field(ProvinceEntity, ProvinceEntity.name, name)
        province = ProvinceEntity(name=name)
        store = get_current_store()
        store.add(province)
