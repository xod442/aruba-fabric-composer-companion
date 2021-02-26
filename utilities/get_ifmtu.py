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

def get_ifMtu_oids(switch_ipaddress):
    counter=0
    ifmtu_list=[]
    errorIndication, errorStatus, errorIndex, varBinds = next(
        getCmd(SnmpEngine(),
            CommunityData('public'),
            UdpTransportTarget((switch_ipaddress, 161)),
            ContextData(),
            # THis OID gets the  number of interfaces
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.4.4')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.4.5')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.4.6')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.4.7')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.4.8')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.4.9')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.4.10')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.4.11')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.4.12')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.4.13')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.4.14')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.4.15')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.4.16')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.4.17')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.4.18')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.4.19')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.4.20')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.4.21')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.4.22')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.4.23')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.4.24')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.4.25')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.4.26')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.4.27')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.4.28')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.4.29')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.4.30')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.4.31')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.4.32')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.4.33')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.4.34')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.4.35')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.4.36')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.4.37')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.4.38')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.4.39')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.4.40')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.4.41')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.4.42')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.4.43')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.4.44')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.4.45')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.4.46')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.4.47')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.4.48')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.4.49')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.4.50')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.4.51')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.4.52')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.4.53')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.4.54')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.4.55')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.4.56')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.4.57')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.4.58')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.4.59')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.4.60')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.4.61')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.4.62')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.4.63')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.4.64')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.4.65')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.4.66')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.4.67')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.4.68')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.4.69')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.4.70')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.4.71')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.4.72')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.4.73')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.4.74')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.4.75'))
            )
        )

    if errorIndication:
        print(errorIndication)
    elif errorStatus:
        print('%s at %s' % (errorStatus.prettyPrint(),errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
    else:
        for varBind in varBinds:
            ifmtu_list.append(str(varBinds[counter][1]))
            counter=counter+1

    return ifmtu_list
