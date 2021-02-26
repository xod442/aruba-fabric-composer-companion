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

from flask import Blueprint, render_template, request, redirect, session, url_for, abort
import os
# from werkzeug import secure_filename
from mongoengine import Q
import pygal
import json
from utilities.get_one_oid import get_oid
# Place to stach the user temporarily
from database.companion import Companion
from pyhpecfm import fabric
from pyhpecfm import system
from utilities.get_client import access_client
from utilities.get_ifdesc import get_ifDesc_oids
from utilities.get_iftype import get_ifType_oids
from utilities.get_ifmtu import get_ifMtu_oids
from utilities.get_ifspeed import get_ifSpeed_oids
from utilities.get_ifadminstatus import get_ifAdminStatus_oids
from utilities.get_ifoperstatus import get_ifOperStatus_oids
from utilities.get_ifinucastpkts import get_ifInUcastPkts_oids
from utilities.get_ifoutucastpkts import get_ifOutUcastPkts_oids
from utilities.switch_array import get_switches

snmp_app=Blueprint('snmp_app', __name__)

@snmp_app.route('/snmp_interface', methods=('GET', 'POST'))
def snmp_interface():
    '''
    Edit an existing entry from the database

    '''
    if request.method == 'POST':
        # Get number of interfaces.

        # Get desired switch_ip
        ipaddress=request.form['ipaddress']

        # Perform the SNMP gets
        ifDesc=get_ifDesc_oids(ipaddress)
        ifType=get_ifType_oids(ipaddress)
        ifMtu=get_ifMtu_oids(ipaddress)
        ifSpeed=get_ifSpeed_oids(ipaddress)
        ifAdminStatus=get_ifAdminStatus_oids(ipaddress)
        ifOperStatus=get_ifOperStatus_oids(ipaddress)
        ifInUcastPkts=get_ifInUcastPkts_oids(ipaddress)
        ifOutUcastPkts=get_ifOutUcastPkts_oids(ipaddress)

        output=[]
        counter=0
        while counter < len(ifDesc):
            # Check the type
            if ifType[counter] == '6':
                XifType='Access'
            else:
                XifType='Fabric'

            # Check the Admin status
            if ifAdminStatus[counter] == '1':
                XifAdminStatus='up'
            elif ifAdminStatus[counter] == '2':
                XifAdminStatus='down'
            else:
                XifAdminStatus='unknown'

            # Check the operation status
            if ifOperStatus[counter] == '1':
                XifOperStatus='up'
            elif ifOperStatus[counter] == '2':
                XifOperStatus='down'
            else:
                XifOperStatus='unknown'

            interface={'interface':counter+1,
                       'ifDesc':ifDesc[counter],
                       'ifType':XifType,
                       'ifMtu':ifMtu[counter],
                       'ifSpeed':ifSpeed[counter],
                       'ifAdminStatus':XifAdminStatus,
                       'ifOperStatus':XifOperStatus,
                       'ifInUcastPkts': ifInUcastPkts[counter],
                       'ifOutUcastPkts':ifOutUcastPkts[counter]
                       }

            output.append(interface)
            counter=counter+1


        #send delete success
        return render_template('snmp/interfaces.html',output=output,ipaddress=ipaddress)

    # Get switch information switch database

    switch_array=get_switches()

    ips=[]
    for switch in switch_array:
        ips.append(switch[1])

    return render_template('snmp/snmp_select_switch.html', switch_ip_list=ips,s=switch_array)
