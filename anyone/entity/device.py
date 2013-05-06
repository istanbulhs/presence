
'''
Created on 02 May 2013

@author: elif
'''

import requests

from spyne.service import ServiceBase
from spyne.decorator import rpc
from spyne.model.primitive import Integer
from spyne.protocol.http import HttpPattern

IP = ''
CLIENTS_URL = "The url where the list of clients is kept"
USER = "modem admin user"
PASSWORD = "password"
SSID = "ssid name"


def get_file():
    html_str = None

    response = requests.get(CLIENTS_URL, auth=(USER, PASSWORD), stream=False)
    html_str = response.text

    return html_str


def count_clients(html_string):
    if html_string is None or "" == html_string:
        return -1
    else:
        return html_string.count(SSID)


class DeviceService(ServiceBase):
    @rpc(_returns=Integer, _http_patterns=[HttpPattern('/kac[-_]?cihaz')])
    def kac_cihaz(self):
        html_content = get_file()
        return count_clients(html_content)
