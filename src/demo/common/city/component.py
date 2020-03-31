# -*- coding: utf-8 -*-
"""
city component module.
"""

from pyrin.application.decorators import component
from pyrin.application.structs import Component

from demo.common.city import CityPackage
from demo.common.city.manager import CityManager


@component(CityPackage.COMPONENT_NAME)
class CityComponent(Component, CityManager):
    """
    city component class.
    """
    pass
