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
username="admin"
ipaddress="10.132.0.219"
password="plexxi"
name="test lag"
description="rak is a wizard"
vlan_uuid="58bd3350-ba6b-4ddb-a575-414e66986245"
a_port_uuid="5b66a496-f440-4746-8a85-1e17af9ace02"
b_port_uuid="129c1b6f-65ad-478d-a7e2-60f8f710b3d1"
speed=10000


# Create client connection
client=CFMClient(ipaddress,username,password)
client.connect()
data = {
    "native_vlan": 0,
    "description": "{}".format(description),
    "vlan_group_uuids": [
            "{}".format(vlan_uuid)
        ],
    "port_properties": [
        {
          "lacp":{
              "priority": 100,
              "intervals": {
                "slow":30,
                "fast":1
           },
           "aggregate_port_limits": {
               "minimum":2,
               "maximum":8
          },
           "mode":"active"
      },
           "speed": {
             "current": int("{}".format(speed))
      },
      "port_uuids": [
         "{}".format(a_port_uuid),
         "{}".format(b_port_uuid)
        ]
      }
    ],
    "ungrouped_vlans": "1",
    "name": "{}".format(name)
}
# params={}
# result = fabric.add_lags(client, name, description, vlan_uuid, a_port_uuid, b_port_uuid, speed)
print data
