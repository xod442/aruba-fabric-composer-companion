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
# __maintainer__ = "Rick Kauffman"
# __email__ = "rick.a.kauffman@hpe.com"

from mongoengine import Q
from database.switches import Switches

def get_switches():

    # Get switch information switch database
    switch_array=[]
    for s in Switches.objects():
        # assigne local variables
        health=s.health
        ip_address=s.ip_address
        mac_address=s.mac_address
        name=s.name
        sw_version=s.sw_version
        uuid=s.uuid
        # Creat a list for the record entry
        out=[health,ip_address,mac_address,name,sw_version,uuid]
        # Make a list of Lists
        switch_array.append(out)

    return switch_array
