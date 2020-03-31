# -*- coding: utf-8 -*-
"""
security component module.
"""

from pyrin.application.decorators import component
from pyrin.application.structs import Component

from demo.security import SecurityPackage
from demo.security.manager import SecurityManager


@component(SecurityPackage.COMPONENT_NAME, replace=True)
class SecurityComponent(Component, SecurityManager):
    """
    security component class.
    """
    pass
