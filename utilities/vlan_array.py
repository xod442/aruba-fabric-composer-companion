# -*-coding: utf-8 -*-
# (C) Copyright 2019 Hewlett Packard Enterprise Development LP.

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#  http://www.apache.org/licenses/LICENSE-2.0

## Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# __author__ = "@netwookie"
# __credits__ = ["Rick Kauffman"]
# __license__ = "Apache2.0"
# __maintainer__ = "Rick Kauffman"
# __email__ = "rick.a.kauffman@hpe.com"

from mongoengine import Q
from database.companion import Companion
from pyhpecfm.client import CFMClient
from pyhpecfm import fabric

def get_vlans():

    # Get user informaation.
    creds=Companion.objects.first()
    username=creds.user.encode('utf-8')
    ipaddress=creds.ipaddress.encode('utf-8')
    password=creds.passwd.encode('utf-8')

    try:
        # Create client connection
        client=CFMClient(ipaddress,username,password)
        client.connect()
    except:
        error='Failed to obtain a client connetion to the CFM controller.'
        return error

    params={}
    cfm_vlans=fabric.get_vlan_groups(client,params)

    return cfm_vlans
