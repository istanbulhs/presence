# encoding: utf8
#
# Copyright © Alternatif Bilisim Dernegi <info at alternatifbilisim dot org>,
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#    1. Redistributions of source code must retain the above copyright notice,
#       this list of conditions and the following disclaimer.
#    2. Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#    3. Neither the name of the owner nor the names of its contributors may be
#       used to endorse or promote products derived from this software without
#       specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER BE LIABLE FOR ANY DIRECT,
# INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY
# OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
# NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
# EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

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
