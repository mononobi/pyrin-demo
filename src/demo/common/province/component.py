# -*- coding: utf-8 -*-
"""
province component module.
"""

from pyrin.application.decorators import component
from pyrin.application.structs import Component

from demo.common.province import ProvincePackage
from demo.common.province.manager import ProvinceManager


@component(ProvincePackage.COMPONENT_NAME)
class ProvinceComponent(Component, ProvinceManager):
    """
    province component class.
    """
    pass
