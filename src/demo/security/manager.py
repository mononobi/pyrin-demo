# -*- coding: utf-8 -*-
"""
security manager module.
"""

import pyrin.security.hashing.services as hashing_services
import pyrin.security.token.services as toke_services
import pyrin.globalization.datetime.services as datetime_services

from pyrin.core.globals import _
from pyrin.core.structs import DTO
from pyrin.database.services import get_current_store
from pyrin.security.authorization.exceptions import UserIsNotActiveError
from pyrin.security.manager import SecurityManager as BaseSecurityManager

from demo.security.exceptions import UserNotFoundError, InvalidUsernameOrPasswordError
from demo.security.models import UserEntity


class SecurityManager(BaseSecurityManager):
    """
    security manager class.
    this class is intended to provide some services needed in pyrin application.
    the top level application must extend this class considering business requirements.
    """

    def has_permission(self, user, permissions, **options):
        """
        gets a value indicating that given user has the specified permissions.

        :param user: user identity to check its permissions.
        :param list[PermissionBase] permissions: permissions to check for user.

        :rtype: bool
        """

        return False

    def login(self, username, password, **options):
        """
        logs in the provided user and gets a valid token.

        :param str username: username.
        :param str password: password.

        :raises InvalidUserInfoError: invalid user info error.
        :raises UserNotFoundError: user not found error.
        :raises UserIsNotActiveError: user is not active error.

        :returns: a valid token.
        :rtype: str
        """

        if username is None or password is None:
            raise InvalidUsernameOrPasswordError(_('Username or password is invalid.'))

        store = get_current_store()
        user = store.query(UserEntity).filter(UserEntity.username == username).one_or_none()

        fail_message = _('User not found, make sure that '
                         'username and password is correct.')
        if user is None:
            raise UserNotFoundError(fail_message)

        if hashing_services.is_match(password, user.password_hash) is not True:
            raise UserNotFoundError(fail_message)

        if user.is_active is False:
            raise UserIsNotActiveError(_('User [{user_id}] is not active.'
                                         .format(user_id=user.id)))

        user.last_login_date = datetime_services.now()
        store.add(user)
        payload = DTO(user_id=user.id)

        return DTO(access_token=toke_services.generate_access_token(payload, is_fresh=True),
                   refresh_token=toke_services.generate_refresh_token(payload))
