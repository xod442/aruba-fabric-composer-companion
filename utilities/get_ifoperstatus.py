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

def get_ifOperStatus_oids(switch_ipaddress):
    counter=0
    ifOperStatus_list=[]
    errorIndication, errorStatus, errorIndex, varBinds = next(
        getCmd(SnmpEngine(),
            CommunityData('public'),
            UdpTransportTarget((switch_ipaddress, 161)),
            ContextData(),
            # THis OID gets the  number of interfaces
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.8.4')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.8.5')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.8.6')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.8.7')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.8.8')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.8.9')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.8.10')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.8.11')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.8.12')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.8.13')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.8.14')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.8.15')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.8.16')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.8.17')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.8.18')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.8.19')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.8.20')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.8.21')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.8.22')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.8.23')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.8.24')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.8.25')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.8.26')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.8.27')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.8.28')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.8.29')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.8.30')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.8.31')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.8.32')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.8.33')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.8.34')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.8.35')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.8.36')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.8.37')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.8.38')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.8.39')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.8.40')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.8.41')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.8.42')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.8.43')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.8.44')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.8.45')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.8.46')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.8.47')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.8.48')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.8.49')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.8.50')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.8.51')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.8.52')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.8.53')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.8.54')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.8.55')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.8.56')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.8.57')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.8.58')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.8.59')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.8.60')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.8.61')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.8.62')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.8.63')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.8.64')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.8.65')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.8.66')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.8.67')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.8.68')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.8.69')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.8.70')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.8.71')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.8.72')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.8.73')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.8.74')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.8.75'))
            )
        )

    if errorIndication:
        print(errorIndication)
    elif errorStatus:
        print('%s at %s' % (errorStatus.prettyPrint(),errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
    else:
        for varBind in varBinds:
            ifOperStatus_list.append(str(varBinds[counter][1]))
            counter=counter+1

    return ifOperStatus_list
