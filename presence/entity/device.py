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


KOMANDOLAR = "Istanbul Hackerspace"


import requests
import presence

from spyne.service import ServiceBase
from spyne.decorator import rpc
from spyne.model.primitive import Integer, Unicode, AnyUri, ImageUri
from spyne.model.primitive import Double, Boolean
from spyne.model.complex import ComplexModel, Array
from spyne.protocol.http import HttpPattern

from spyne.util.invregexp import invregexp

class SpaceLocation(ComplexModel):
    address = Unicode
    lon = Double
    lat = Double


class SpaceContact(ComplexModel):
    twitter = Unicode(pattern="@[a-z0-9]+")
    # burayi doldurmak gerekecek

IssueReportChannel = Unicode(values=["twitter"], # bunu da
                                type_name="IssueReportChannelType")

class SpaceState(ComplexModel):
    open = Boolean


class SpaceStatus(ComplexModel):
    _type_info = [
        ("api", Unicode(default=u"0.13")),
        ("space", Unicode),
        ("logo", ImageUri),
        ("url", AnyUri),
        ("location", SpaceLocation),
        ("contact", SpaceContact),
        ("issue_report_channels", Array(IssueReportChannel)),
        ("state", SpaceState),
    ]


def get_file():
    html_str = None

    url = presence.config['modem']['url']
    user = presence.config['modem']['user']
    password = presence.config['modem']['password']

    response = requests.get(url, auth=(user, password), stream=False)
    html_str = response.text

    return html_str


def count_clients(html_string):
    ssid = presence.config['modem']['ssid']

    if html_string is None or "" == html_string:
        return -1
    else:
        return html_string.count(ssid)

def hackerspace_status(html_string):
    ssid = presence.config['modem']['ssid']

    if html_string is None or "" == html_string:
        return None
    else
        count = html_string.count(ssid)
        if(count == 0)
            return False
        else
            return True

class DeviceService(ServiceBase):
    @rpc(_returns=Integer,
         _patterns=[HttpPattern(p) for p in invregexp('/kac[_-]?cihaz/?')])
    def kac_cihaz(self):
        html_content = get_file()
        return count_clients(html_content)

    @rpc(_returns=SpaceStatus)
    def presence(self):
        # buradaki verinin bir kısmını constant olarak yukarıya mı alsak?
        return SpaceStatus(
            space=KOMANDOLAR,
            logo="http://s.gravatar.com/avatar/3c9fcdce41f596d8d9d4432a606e14de?s=80",
            url="https://www.istanbulhs.org",
            location=SpaceLocation(
                lat=40.993498,
                lon=29.042059,
                address=u"Eğitim Mah. Ömerbey (Çıkmaz) Sokak. No:19/B Kadıköy/İSTANBUL",
            ),
            contact=SpaceContact(
                twitter="@istanbulhs"
            ),
            issue_report_channels=["twitter"],
            state=SpaceState(
                open=hackerspace_status(get_file()),
            )
        )
