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

def get_ifType_oids(switch_ipaddress):
    counter=0
    iftype_list=[]
    errorIndication, errorStatus, errorIndex, varBinds = next(
        getCmd(SnmpEngine(),
            CommunityData('public'),
            UdpTransportTarget((switch_ipaddress, 161)),
            ContextData(),
            # THis OID gets the  number of interfaces
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.3.4')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.3.5')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.3.6')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.3.7')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.3.8')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.3.9')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.3.10')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.3.11')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.3.12')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.3.13')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.3.14')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.3.15')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.3.16')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.3.17')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.3.18')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.3.19')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.3.20')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.3.21')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.3.22')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.3.23')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.3.24')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.3.25')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.3.26')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.3.27')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.3.28')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.3.29')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.3.30')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.3.31')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.3.32')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.3.33')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.3.34')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.3.35')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.3.36')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.3.37')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.3.38')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.3.39')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.3.40')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.3.41')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.3.42')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.3.43')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.3.44')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.3.45')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.3.46')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.3.47')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.3.48')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.3.49')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.3.50')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.3.51')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.3.52')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.3.53')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.3.54')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.3.55')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.3.56')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.3.57')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.3.58')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.3.59')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.3.60')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.3.61')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.3.62')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.3.63')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.3.64')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.3.65')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.3.66')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.3.67')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.3.68')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.3.69')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.3.70')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.3.71')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.3.72')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.3.73')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.3.74')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.3.75'))
            )
        )

    if errorIndication:
        print(errorIndication)
    elif errorStatus:
        print('%s at %s' % (errorStatus.prettyPrint(),errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
    else:
        for varBind in varBinds:
            iftype_list.append(str(varBinds[counter][1]))
            counter=counter+1

    return iftype_list
