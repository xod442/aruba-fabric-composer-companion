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


counter=0
ifdesc_list=[]
errorIndication, errorStatus, errorIndex, varBinds = next(
    getCmd(SnmpEngine(),
        CommunityData('public'),
        UdpTransportTarget(('172.18.31.1', 161)),
        ContextData(),
        # THis OID gets the  number of interfaces
        ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.2.4')),
        ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.2.5')),
        ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.2.6')),
        ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.2.7')),
        ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.2.8')),
        ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.2.9')),
        ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.2.10')),
        ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.2.11')),
        ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.2.12')),
        ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.2.13')),
        ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.2.14')),
        ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.2.15')),
        ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.2.16')),
        ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.2.17')),
        ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.2.18')),
        ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.2.19')),
        ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.2.20')),
        ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.2.21')),
        ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.2.22')),
        ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.2.23')),
        ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.2.24')),
        ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.2.25')),
        ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.2.26')),
        ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.2.27')),
        ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.2.28')),
        ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.2.29')),
        ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.2.30')),
        ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.2.31')),
        ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.2.32')),
        ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.2.33')),
        ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.2.34')),
        ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.2.35')),
        ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.2.36')),
        ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.2.37')),
        ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.2.38')),
        ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.2.39')),
        ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.2.40')),
        ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.2.41')),
        ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.2.42')),
        ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.2.43')),
        ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.2.44')),
        ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.2.45')),
        ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.2.46')),
        ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.2.47')),
        ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.2.48')),
        ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.2.49')),
        ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.2.50')),
        ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.2.51')),
        ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.2.52')),
        ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.2.53')),
        ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.2.54')),
        ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.2.55')),
        ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.2.56')),
        ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.2.57')),
        ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.2.58')),
        ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.2.59')),
        ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.2.60')),
        ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.2.61')),
        ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.2.62')),
        ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.2.63')),
        ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.2.64')),
        ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.2.65')),
        ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.2.66')),
        ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.2.67')),
        ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.2.68')),
        ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.2.69')),
        ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.2.70')),
        ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.2.71')),
        ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.2.72')),
        ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.2.73')),
        ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.2.74')),
        ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.2.75'))
        )
    )

if errorIndication:
    print(errorIndication)
elif errorStatus:
    print('%s at %s' % (errorStatus.prettyPrint(),errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
else:
    for varBind in varBinds:
        print varBinds[counter][0]
        ifdesc_list.append(str(varBinds[counter][1]))
        counter=counter+1

print ifdesc_list
