#!/usr/bin/env python

"""proxymr.py: seteo proxy para notebooks."""

__author__ = "Marco Redondo"
__email__ = "redondomarco@gmail.com"
__status__ = "Devel"

import os
def set_proxy():
    #proxy_addr = 'http://{user}:{passwd}@{address}:{port}'.format(
    #    user='user_example', passwd='pass_example', 
    #    address='address_example', port=int('port_example'))
    proxy_addr = 'http://proxysvc.svc.rosario.gov.ar:3128'
    os.environ['http_proxy'] = proxy_addr
    os.environ['https_proxy'] = proxy_addr