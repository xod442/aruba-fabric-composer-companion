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

def get_ifAdminStatus_oids(switch_ipaddress):
    counter=0
    ifAdminStatus_list=[]
    errorIndication, errorStatus, errorIndex, varBinds = next(
        getCmd(SnmpEngine(),
            CommunityData('public'),
            UdpTransportTarget((switch_ipaddress, 161)),
            ContextData(),
            # THis OID gets the  number of interfaces
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.7.4')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.7.5')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.7.6')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.7.7')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.7.8')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.7.9')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.7.10')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.7.11')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.7.12')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.7.13')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.7.14')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.7.15')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.7.16')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.7.17')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.7.18')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.7.19')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.7.20')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.7.21')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.7.22')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.7.23')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.7.24')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.7.25')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.7.26')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.7.27')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.7.28')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.7.29')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.7.30')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.7.31')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.7.32')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.7.33')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.7.34')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.7.35')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.7.36')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.7.37')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.7.38')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.7.39')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.7.40')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.7.41')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.7.42')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.7.43')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.7.44')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.7.45')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.7.46')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.7.47')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.7.48')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.7.49')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.7.50')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.7.51')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.7.52')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.7.53')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.7.54')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.7.55')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.7.56')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.7.57')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.7.58')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.7.59')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.7.60')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.7.61')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.7.62')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.7.63')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.7.64')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.7.65')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.7.66')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.7.67')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.7.68')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.7.69')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.7.70')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.7.71')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.7.72')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.7.73')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.7.74')),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.7.75'))
            )
        )

    if errorIndication:
        print(errorIndication)
    elif errorStatus:
        print('%s at %s' % (errorStatus.prettyPrint(),errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
    else:
        for varBind in varBinds:
            #ifAdminStatus_list.append(str(varBinds[counter]))
            ifAdminStatus_list.append(str(varBinds[counter][1]))
            counter=counter+1

    return ifAdminStatus_list
