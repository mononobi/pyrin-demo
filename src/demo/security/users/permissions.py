# -*- coding: utf-8 -*-
"""
users permissions module.
"""

from demo.security.permission.base import CorePermission


VIEW_USERS_LIST_PERMISSION = CorePermission(1, 'View users list.')
