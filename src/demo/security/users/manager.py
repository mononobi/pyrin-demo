# -*- coding: utf-8 -*-
"""
users manager module.
"""

import pyrin.security.services as security_services

from pyrin.database.services import get_current_store
from pyrin.security.session.services import get_current_user
from pyrin.core.globals import _
from pyrin.security.users.manager import UsersManager as BaseUsersManager

from demo.security.exceptions import UserNotFoundError
from demo.security.models import UserEntity
from demo.security.users.exceptions import InvalidUserIDError


class UsersManager(BaseUsersManager):
    """
    users manager class.
    """

    def _get(self, user_id, **options):
        """
        gets the specified user.

        :param int user_id: user id to get its info.

        :raises UserNotFoundError: user not found error.

        :rtype: UserEntity
        """

        store = get_current_store()
        user = store.query(UserEntity).get(user_id)

        if user is None:
            raise UserNotFoundError(_('User [{user_id}] not found.'.format(user_id=user_id)))

        return user

    def get(self, **options):
        """
        gets the current user info.

        :raises UserNotFoundError: user not found error.

        :rtype: UserEntity
        """

        user_id = get_current_user()
        return self._get(user_id, **options)

    def _exists(self, user_id):
        """
        gets a value indicating that given user existed.

        :param int user_id: user id to check for existence.

        :raises InvalidUserError: invalid user error.

        :rtype: bool
        """

        if user_id is None:
            raise InvalidUserIDError(_('Input user id could not be None.'))

        store = get_current_store()
        count = store.query(UserEntity.id).filter(UserEntity.id == user_id).count()

        return count > 0

    def is_active(self, user, **options):
        """
        gets a value indicating that given user is active.

        :param int user: user to check its active status.

        :raises InvalidUserError: invalid user error.
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

        entity = UserEntity()
        entity.username = username
        entity.password_hash = security_services.get_password_hash(password)
        entity.first_name = first_name
        entity.last_name = last_name
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
        return store.query(UserEntity).all()
