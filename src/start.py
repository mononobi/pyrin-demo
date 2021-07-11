# -*- coding: utf-8 -*-
"""
main entry point for demo application.
"""

from demo import DemoApplication


app = DemoApplication()

if __name__ == '__main__':
    app.run(use_reloader=False)
