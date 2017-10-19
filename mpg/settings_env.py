import socket

"""
Check Enviroment
"""

try:
    from .settings_dev import *
except ImportError as e:
    from .settings_prod import *
