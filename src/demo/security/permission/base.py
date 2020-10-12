# -*- coding: utf-8 -*-
"""
permission base module.
"""

from pyrin.core.globals import SECURE_TRUE
from pyrin.security.permission.base import PermissionBase

from demo.security.permission.models import PermissionEntity


class CorePermission(PermissionBase):
    """
    core permission class.

    all application permissions must be an instance of this.
    """

    def __init__(self, permission_id, description, **options):
        """
        initializes an instance of CorePermission.

        :param int permission_id: permission id.
        :param str description: permission description.
        """

        self.id = permission_id
        self.description = description

        super().__init__(**options)

    def __hash__(self):
        return hash(self.get_id())

    def __eq__(self, other):
        if not isinstance(other, CorePermission):
            return False

        return other.get_id() == self.get_id()

    def __ne__(self, other):
        return not self == other

    def __str__(self):
        return '{id}-{description}'.format(id=self.get_id(), description=self.description)

    def __repr__(self):
        return str(self)

    def to_entity(self):
        """
        gets the equivalent entity of current permission.

        :rtype: PermissionEntity
        """

        entity = PermissionEntity(id=self.id,
                                  description=self.description,
                                  populate_all=SECURE_TRUE)
        return entity

    def get_id(self):
        """
        gets permission id.
        note that this object must be fully unique for each different permission.

        :rtype: str
        """

        return self.id
