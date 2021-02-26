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

def get_ifPhysAddress_oids(switch_ipaddress):
    counter=0
    ifPhysAddress_list=[]
    errorIndication, errorStatus, errorIndex, varBinds = next(
        getCmd(SnmpEngine(),
            CommunityData('public'),
            UdpTransportTarget((switch_ipaddress, 161)),
            ContextData(),
            # THis OID gets the  number of interfaces
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.6.4')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.6.5')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.6.6')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.6.7')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.6.8')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.6.9')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.6.10')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.6.11')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.6.12')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.6.13')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.6.14')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.6.15')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.6.16')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.6.17')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.6.18')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.6.19')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.6.20')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.6.21')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.6.22')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.6.23')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.6.24')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.6.25')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.6.26')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.6.27')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.6.28')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.6.29')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.6.30')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.6.31')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.6.32')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.6.33')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.6.34')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.6.35')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.6.36')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.6.37')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.6.38')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.6.39')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.6.40')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.6.41')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.6.42')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.6.43')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.6.44')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.6.45')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.6.46')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.6.47')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.6.48')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.6.49')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.6.50')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.6.51')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.6.52')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.6.53')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.6.54')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.6.55')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.6.56')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.6.57')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.6.58')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.6.59')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.6.60')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.6.61')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.6.62')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.6.63')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.6.64')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.6.65')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.6.66')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.6.67')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.6.68')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.6.69')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.6.70')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.6.71')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.6.72')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.6.73')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.6.74')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.6.75'))
            )
        )

    if errorIndication:
        print(errorIndication)
    elif errorStatus:
        print('%s at %s' % (errorStatus.prettyPrint(),errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
    else:
        for varBind in varBinds:
            ifPhysAddress_list.append(str(varBinds[counter][1]))
            #ifPhysAddress_list.append(str(varBinds[counter]))
            counter=counter+1

    return ifPhysAddress_list
