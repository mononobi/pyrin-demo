# -*- coding: utf-8 -*-
"""
demo application main package.
"""

from pyrin.application.base import Application


class DemoApplication(Application):
    """
    demo application class.

    server should create an instance of this class on startup.
    """

    def get_application_version(self):
        """
        gets application version.

        :rtype: str
        """

        return '0.1'
