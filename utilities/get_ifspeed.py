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

def get_ifSpeed_oids(switch_ipaddress):
    counter=0
    ifSpeed_list=[]
    errorIndication, errorStatus, errorIndex, varBinds = next(
        getCmd(SnmpEngine(),
            CommunityData('public'),
            UdpTransportTarget((switch_ipaddress, 161)),
            ContextData(),
            # THis OID gets the  number of interfaces
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.5.4')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.5.5')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.5.6')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.5.7')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.5.8')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.5.9')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.5.10')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.5.11')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.5.12')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.5.13')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.5.14')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.5.15')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.5.16')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.5.17')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.5.18')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.5.19')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.5.20')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.5.21')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.5.22')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.5.23')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.5.24')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.5.25')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.5.26')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.5.27')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.5.28')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.5.29')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.5.30')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.5.31')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.5.32')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.5.33')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.5.34')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.5.35')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.5.36')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.5.37')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.5.38')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.5.39')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.5.40')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.5.41')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.5.42')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.5.43')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.5.44')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.5.45')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.5.46')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.5.47')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.5.48')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.5.49')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.5.50')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.5.51')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.5.52')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.5.53')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.5.54')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.5.55')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.5.56')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.5.57')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.5.58')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.5.59')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.5.60')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.5.61')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.5.62')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.5.63')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.5.64')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.5.65')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.5.66')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.5.67')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.5.68')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.5.69')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.5.70')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.5.71')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.5.72')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.5.73')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.5.74')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.5.75'))
            )
        )

    if errorIndication:
        print(errorIndication)
    elif errorStatus:
        print('%s at %s' % (errorStatus.prettyPrint(),errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
    else:
        for varBind in varBinds:
            ifSpeed_list.append(str(varBinds[counter][1]))
            counter=counter+1

    return ifSpeed_list
