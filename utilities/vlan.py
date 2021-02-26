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
# __email__ = "rick.a.kauffman@hpe.co
from pyhpecfm.client import CFMClient
from pyhpecfm import fabric

# Get user informaation.
username='admin'
ipaddress='10.132.0.219'
password='plexxi'
name='test vlan'
description='rak is a wizard'
vlans='1000'


# Create client connection
client=CFMClient(ipaddress,username,password)
client.connect()

params={}
result = fabric.add_vlan_groups(client, name, description, vlans)
print result
