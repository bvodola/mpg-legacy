import socket

"""
Check Enviroment
"""

try:
    from .settings_dev_ import *
except ImportError as e:
    from .settings_prod import *
