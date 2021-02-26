# -*-coding: utf-8 -*-
# (C) Copyright 2019 Hewlett Packard Enterprise Development LP.

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#  http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# __author__ = "@netwookie"
# __credits__ = ["Rick Kauffman"]
# __license__ = "Apache2.0"
# __version__ = "1.0.0"
# __maintainer__ = "Rick Kauffman"
# __email__ = "rick.a.kauffman@hpe.com"

#SNMPv2c

# Send SNMP GET request using the following options:

#* with SNMPv2c, community 'public'
# * over IPv4/UDP
# * to an Agent at demo.snmplabs.com:161
# * for two OIDs in string form

# Functionally similar to:

# | $ snmpget -v2c -c public demo.snmplabs.com 1.3.6.1.2.1.1.1.0 1.3.6.1.2.1.1.6.0

from pysnmp.hlapi import *
from pysnmp.smi import *
from pysnmp.proto import *
from pysnmp.entity import *
from pysnmp.carrier import *


def get_oid(oid, switch_ipaddress):

    errorIndication, errorStatus, errorIndex, varBinds = next(
        getCmd(SnmpEngine(),
            CommunityData('public'),
            UdpTransportTarget((switch_ipaddress, 161)),
            ContextData(),
            # THis OID gets the  number of interfaces
            ObjectType(ObjectIdentity(oid)))
        )


    if errorIndication:
        print(errorIndication)
    elif errorStatus:
        print('%s at %s' % (errorStatus.prettyPrint(),errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
    else:
        result = varBinds[0][1]
        return result
