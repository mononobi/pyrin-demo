# -*- coding: utf-8 -*-
"""
main entry point for demo application.
"""

from demo import DemoApplication


app = DemoApplication()

# the if condition is to ensure that multiprocessing
# on windows works as expected.
if __name__ == '__main__':
    app.run(use_reloader=False)
