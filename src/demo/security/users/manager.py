# -*- coding: utf-8 -*-
"""
users manager module.
"""

import pyrin.security.services as security_services
import pyrin.validator.services as validator_services

from pyrin.core.globals import _, SECURE_TRUE
from pyrin.core.structs import DTO
from pyrin.database.services import get_current_store
from pyrin.security.session.services import get_current_user
from pyrin.security.users.manager import UsersManager as BaseUsersManager

from demo.security.exceptions import UserNotFoundError
from demo.security.models import UserEntity


class UsersManager(BaseUsersManager):
    """
    users manager class.
    """

    def _get(self, id, **options):
        """
        gets the specified user.

        :param int id: user id to get its info.

        :raises UserNotFoundError: user not found error.

        :rtype: UserEntity
        """

        data = validator_services.validate(UserEntity, id=id)
        store = get_current_store()
        user = store.query(UserEntity).get(data.get(id))

        if user is None:
            raise UserNotFoundError(_('User [{user_id}] not found.'.format(user_id=data.get(id))))

        return user

    def get_info(self, **options):
        """
        gets the current user info.

        :rtype: UserEntity
        """

        user_id = get_current_user()
        return self._get(user_id, **options)

    def _exists(self, id):
        """
        gets a value indicating that given user existed.

        :param int id: user id to check for existence.

        :rtype: bool
        """

        data = validator_services.validate(UserEntity, id=id)
        store = get_current_store()
        return store.query(UserEntity.id).filter(UserEntity.id == data.get(id)).existed()

    def is_active(self, user, **options):
        """
        gets a value indicating that given user is active.

        :param int user: user to check its active status.

        :raises UserNotFoundError: user not found error.

        :rtype: bool
        """

        if self._exists(user) is not True:
            raise UserNotFoundError(_('User [{user}] not found.').format(user=user))

        user_info = self._get(user, **options)
        return user_info.is_active

    def create(self, username, password, first_name, last_name, **options):
        """
        creates a new user based on given inputs.

        :param str username: username.
        :param str password: password.
        :param str first_name: first name.
        :param str last_name: last name.
        """

        data = DTO(username=username, password=password,
                   first_name=first_name, last_name=last_name)
        validator_services.validate_dict(UserEntity, data)
        entity = UserEntity(**data)
        entity.password_hash = security_services.get_password_hash(data.password)
        entity.is_active = True

        store = get_current_store()
        store.add(entity)

    def get_all(self, **options):
        """
        gets a list of all users.

        :returns: list[UserEntity]
        :rtype: list
        """

        store = get_current_store()
        return store.query(UserEntity).paginate(inject_total=SECURE_TRUE, **options).all()
