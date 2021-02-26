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

def get_ifInUcastPkts_oids(switch_ipaddress):
    counter=0
    ifInUcastPkts_list=[]
    errorIndication, errorStatus, errorIndex, varBinds = next(
        getCmd(SnmpEngine(),
            CommunityData('public'),
            UdpTransportTarget((switch_ipaddress, 161)),
            ContextData(),
            # THis OID gets the  number of interfaces
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.11.4')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.11.5')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.11.6')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.11.7')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.11.8')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.11.9')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.11.10')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.11.11')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.11.12')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.11.13')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.11.14')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.11.15')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.11.16')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.11.17')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.11.18')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.11.19')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.11.20')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.11.21')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.11.22')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.11.23')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.11.24')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.11.25')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.11.26')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.11.27')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.11.28')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.11.29')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.11.30')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.11.31')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.11.32')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.11.33')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.11.34')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.11.35')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.11.36')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.11.37')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.11.38')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.11.39')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.11.40')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.11.41')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.11.42')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.11.43')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.11.44')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.11.45')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.11.46')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.11.47')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.11.48')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.11.49')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.11.50')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.11.51')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.11.52')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.11.53')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.11.54')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.11.55')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.11.56')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.11.57')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.11.58')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.11.59')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.11.60')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.11.61')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.11.62')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.11.63')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.11.64')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.11.65')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.11.66')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.11.67')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.11.68')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.11.69')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.11.70')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.11.71')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.11.72')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.11.73')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.11.74')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.11.75'))
            )
        )

    if errorIndication:
        print(errorIndication)
    elif errorStatus:
        print('%s at %s' % (errorStatus.prettyPrint(),errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
    else:
        for varBind in varBinds:
            ifInUcastPkts_list.append(str(varBinds[counter][1]))
            counter=counter+1

    return ifInUcastPkts_list
