import socket

"""
Check Enviroment
"""

DEV_HOST = 'DESKTOP-P478I4P'
UBUNTU_DEV_HOST = 'PCdoB'
PROD_HOST_402 = 'web402.webfaction.com'
PROD_HOST_506 = 'web506.webfaction.com'

if socket.gethostname() == DEV_HOST:
	from .settings_dev import *
if socket.gethostname() == UBUNTU_DEV_HOST:
	from .settings_dev import *
elif socket.gethostname() == PROD_HOST_402:
	from .settings_prod_402 import *
elif socket.gethostname() == PROD_HOST_506:
	from .settings_prod_506 import *
else:
	raise Exception("Cannot determine execution mode for host '%s'.  Please check DEV_HOST and PROD_HOST in settings_env.py." %socket.gethostname())