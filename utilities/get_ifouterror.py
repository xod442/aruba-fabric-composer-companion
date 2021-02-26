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

def get_ifOutError_oids(switch_ipaddress):
    counter=0
    ifOutError_list=[]
    errorIndication, errorStatus, errorIndex, varBinds = next(
        getCmd(SnmpEngine(),
            CommunityData('public'),
            UdpTransportTarget((switch_ipaddress, 161)),
            ContextData(),
            # THis OID gets the  number of interfaces
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.20.4')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.20.5')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.20.6')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.20.7')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.20.8')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.20.9')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.20.10')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.20.11')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.20.12')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.20.13')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.20.14')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.20.15')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.20.16')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.20.17')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.20.18')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.20.19')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.20.20')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.20.21')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.20.22')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.20.23')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.20.24')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.20.25')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.20.26')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.20.27')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.20.28')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.20.29')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.20.30')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.20.31')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.20.32')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.20.33')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.20.34')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.20.35')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.20.36')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.20.37')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.20.38')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.20.39')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.20.40')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.20.41')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.20.42')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.20.43')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.20.44')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.20.45')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.20.46')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.20.47')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.20.48')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.20.49')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.20.50')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.20.51')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.20.52')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.20.53')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.20.54')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.20.55')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.20.56')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.20.57')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.20.58')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.20.59')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.20.60')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.20.61')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.20.62')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.20.63')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.20.64')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.20.65')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.20.66')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.20.67')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.20.68')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.20.69')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.20.70')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.20.71')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.20.72')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.20.73')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.20.74')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.20.75'))
            )
        )

    if errorIndication:
        print(errorIndication)
    elif errorStatus:
        print('%s at %s' % (errorStatus.prettyPrint(),errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
    else:
        for varBind in varBinds:
            ifOutError_list.append(str(varBinds[counter][1]))
            counter=counter+1

    return ifOutError_list
