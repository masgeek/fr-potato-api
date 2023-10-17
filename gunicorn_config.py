"""
Gunicorn configuration file.

"""
import os

import gunicorn

bind_ip = os.getenv('bind_ip', '0.0.0.0')
bind_port = os.getenv('bind_port', '5000')
bind = '{0}:{1}'.format(bind_ip, bind_port)
capture_output = True
accesslog = '-'

# keyfile = os.getenv('ssl_key_path')
# certfile = os.getenv('ssl_cert_path')
workers = 2
loglevel = os.getenv('LOG_LEVEL', 'INFO').lower()

gunicorn.SERVER_SOFTWARE = ''
