import socket

#My laptop is name 'Guinsly-thinkpad-lenovo'
if not 'jebrellish' in socket.gethostname():
    from .development import *
    print('--dev--settings--')
else:
    # if you cloned this app
    # rename the file settings/production_py_example to
    # production.py
    from .production import *
    #print('prod--settings')
#this file won't be load in git and in the
