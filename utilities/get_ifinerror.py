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

def get_ifInError_oids(switch_ipaddress):
    counter=0
    ifInError_list=[]
    errorIndication, errorStatus, errorIndex, varBinds = next(
        getCmd(SnmpEngine(),
            CommunityData('public'),
            UdpTransportTarget((switch_ipaddress, 161)),
            ContextData(),
            # THis OID gets the  number of interfaces
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.14.4')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.14.5')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.14.6')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.14.7')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.14.8')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.14.9')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.14.10')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.14.11')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.14.12')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.14.13')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.14.14')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.14.15')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.14.16')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.14.17')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.14.18')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.14.19')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.14.20')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.14.21')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.14.22')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.14.23')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.14.24')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.14.25')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.14.26')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.14.27')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.14.28')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.14.29')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.14.30')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.14.31')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.14.32')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.14.33')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.14.34')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.14.35')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.14.36')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.14.37')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.14.38')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.14.39')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.14.40')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.14.41')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.14.42')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.14.43')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.14.44')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.14.45')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.14.46')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.14.47')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.14.48')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.14.49')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.14.50')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.14.51')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.14.52')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.14.53')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.14.54')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.14.55')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.14.56')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.14.57')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.14.58')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.14.59')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.14.60')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.14.61')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.14.62')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.14.63')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.14.64')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.14.65')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.14.66')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.14.67')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.14.68')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.14.69')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.14.70')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.14.71')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.14.72')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.14.73')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.14.74')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.14.75'))
            )
        )

    if errorIndication:
        print(errorIndication)
    elif errorStatus:
        print('%s at %s' % (errorStatus.prettyPrint(),errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
    else:
        for varBind in varBinds:
            ifInError_list.append(str(varBinds[counter][1]))
            counter=counter+1

    return ifInError_list
