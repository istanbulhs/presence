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

import logging
logger = logging.getLogger(__name__)

import os
import yaml
import presence

from spyne.protocol.http import HttpRpc
from spyne.protocol.json import JsonDocument
from spyne.server.wsgi import WsgiApplication

from presence.application import MyApplication

from presence.entity.device import DeviceService

from wsgiref.simple_server import make_server

def main():
    if not os.path.isfile('config.yaml'):
        raise Exception(
               "'config.yaml' bulunamadi. once config dosyasini bir yaziverin.")

    presence.config = yaml.load(open('config.yaml', 'r').read())

    logging.basicConfig(level=logging.DEBUG)

    application = MyApplication([DeviceService],
                'http://istanbulhs.org/api',
                in_protocol=HttpRpc(validator='soft'),
                out_protocol=JsonDocument(ignore_wrappers=True),
            )

    wsgi_app = WsgiApplication(application)
    host = presence.config['daemon']['host']
    port = int(presence.config['daemon']['port'])
    server = make_server(host, port, wsgi_app)

    logging.info("listening to http://%s:%d", host, port)
    logging.info("wsdl is at: http://localhost:8000/?wsdl")

    return server.serve_forever()
