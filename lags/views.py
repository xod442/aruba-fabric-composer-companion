# -*- coding: utf-8 -*-
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
#
#   a python module that handles the link-aggregation API call to the CFM controller
#
#---------------------------------------------------------------------------------------
from flask import Blueprint, render_template, request, redirect, session, url_for, abort
import os
# from werkzeug import secure_filename
from mongoengine import Q
import pygal
import json

# Place to stach the user temporarily
from database.companion import Companion
from database.ports import Ports
from database.b_ports import b_Ports
from pyhpecfm.client import CFMClient
from pyhpecfm import fabric
from pyhpecfm import system
from utilities.get_client import access_client
from utilities.switch_array import get_switches
from utilities.port_array import get_ports
from utilities.vlan_array import get_vlans

lag_app=Blueprint('lag_app', __name__)

@lag_app.route('/process_lags', methods=('GET', 'POST'))
def process_lags():

    # Get a client connection.
    client=access_client()

    # assignment of attributes
    count_only=False
    mac_attachments=True
    mac_learning=True
    ports=True
    port_type='access'
    tags=True
    type='provisioned'
    vlan_groups=True
    # Create an attribute dictionary
    params={
            'count_only': count_only,
            'mac_attachments': mac_attachments,
            'mac_learning': mac_learning,
            'ports': ports,
            'port_type': port_type,
            'tags': tags,
            'type': type,
            'vlan_groups': vlan_groups
        }

   # Pull the CFM controller for all lags
    try:
        cfm_lags=fabric.get_lags(client, params)
    except:
        error="ERR-LOGIN - Failed to log into CFM controller"
        return error

    # build properties and ports disctionaries
    # Create some empty lists
    port_props=[]
    port_detail=[]
    lag_group=[]
    for lag in cfm_lags:
        if len(lag['port_properties']) > 1:

            # Iterate through port_properties
            for item in lag['port_properties']:
                lag_mode=item['lacp']['mode']
                lag_speed=item['speed']['current']
                lag_partner_status=item['port_lacp_state'][0]['partner_state_lacp_status']
                lag_partner_system=item['port_lacp_state'][0]['partner_state_system_id']
                lag_partner_port_state=item['port_lacp_state'][0]['partner_state_port']
                actor_lacp_status=item['port_lacp_state'][0]['actor_state_lacp_status']
                # Define properties dictionary
                properties={
                     'mode':lag_mode,
                     'speed':lag_speed,
                     'partner_status':lag_partner_status,
                     'partner_system':lag_partner_system,
                     'partner_port_state':lag_partner_port_state,
                     'actor_status':actor_lacp_status
                    }

                # Extract port detail.
                for ports in item['ports']:
                    switch_name=ports['switch_name']
                    link_state=ports['link_state']
                    admin_state=ports['admin_state']
                    port_security_enabled=ports['port_security_enabled']
                    vlans=ports['vlans']
                    speed=ports['speed']
                    port_label=ports['port_label']
                    bridge_loop_detection=ports['bridge_loop_detection']
                # Define port dictionary
                port_information={
                    'switch_name': switch_name,
                    'link_state': link_state,
                    'admin_state': admin_state,
                    'port_security_enabled': port_security_enabled,
                    'vlans': vlans,
                    'speed': speed,
                    'port_label': port_label,
                    'bridge_loop_detection': bridge_loop_detection
                    }

                port_detail.append(port_information)
                #ports = {'ports':port_detail}
            #----add port detail to the dictionary items
            properties['ports']=port_detail
            properties['name']=lag['name']
            # Now make it a dictionary
            properties={'properties': properties}

            lag_group.append(properties)


        lag_data=[]
        port_props=[]
        port_detail=[]
    return render_template('lags/lags.html', l=lag_group)

@lag_app.route('/autolag', methods=('GET', 'POST'))
def autolag():

    # Clear ports database on new session.
    Ports.objects().delete()

    # Clear ports database on new session.
    b_Ports.objects().delete()

    switch_list_out=[]
    switch_list=[]

    vlan_list_out=[]
    vlan_list=[]

    # Get a client connection.
    switches=get_switches()
    for switch in switches:
        switch_name=switch[3].encode('utf-8')
        switch_uuid=switch[5].encode('utf-8')
        switch_list=[switch_name,switch_uuid]
        switch_list_out.append(switch_list)

    # Get a client connection.
    vlans=get_vlans()
    for vlan in vlans:
        vlansx=vlan['vlans'].encode('utf-8')
        uuid=vlan['uuid'].encode('utf-8')
        vlan_list=[vlansx,uuid]
        vlan_list_out.append(vlan_list)

    count = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48]

    return render_template('lags/autolag.html', switches=switch_list_out, vlans=vlan_list_out, count=count)


@lag_app.route('/makelags', methods=('GET', 'POST'))
def makelags():

    # Get a client connection.
    client=access_client()

    a_list=[]
    a_list_out=[]
    b_list=[]
    b_list_out=[]


    #Get items from the chooser    rick.append('fail')
    vlan_uuid=request.form['vlan'].encode('utf-8')
    a_switch=request.form['a_switch'].encode('utf-8')
    b_switch=request.form['b_switch'].encode('utf-8')
    count=request.form['count'].encode('utf-8')
    count = int(count)


    # Verify selections
    if a_switch == b_switch:
        error="ERR009 - You picked the same switches. Please pick two different switches"
        return render_template('Companion/dberror.html', error=error)

    if a_switch == 'no select' or b_switch == 'no select' or vlan_uuid == 'no select':
        error="ERR00910 - You missed a selection. Make sure to select valid items"
        return render_template('Companion/dberror.html', error=error)


    # Build a side ports database

    port_info=[]
    port_info_out=[]
    ports=get_ports()
    for port in ports:
        if port['switch_uuid'] == a_switch:
            speed=port['speed']['current']
            speed=str(speed)
            speed=speed.encode('utf-8')
            uuid=port['uuid'].encode('utf-8')
            port_label=port['port_label'].encode('utf-8')
            silkscreen=port['silkscreen'].encode('utf-8')
            switch_uuid=port['switch_uuid'].encode('utf-8')
            # Build database entry to save creds
            port = Ports(speed=speed,uuid=uuid,switch_uuid=switch_uuid,port_label=port_label,silkscreen=silkscreen)
            # Save the record
            try:
                port.save()
            except:
                error="ERR001 - Failed to save port information"
                return render_template('Companion/dberror.html', error=error)

    # Build b side ports database
    port_info=[]
    port_info_out=[]
    ports=get_ports()
    for port in ports:
        if port['switch_uuid'] == b_switch:
            speed=port['speed']['current']
            speed=str(speed)
            speed=speed.encode('utf-8')
            uuid=port['uuid'].encode('utf-8')
            port_label=port['port_label'].encode('utf-8')
            silkscreen=port['silkscreen'].encode('utf-8')
            switch_uuid=port['switch_uuid'].encode('utf-8')
            # Build database entry to save creds
            port = b_Ports(speed=speed,uuid=uuid,switch_uuid=switch_uuid,port_label=port_label,silkscreen=silkscreen)
            # Save the record
            try:
                port.save()
            except:
                error="ERR001 - Failed to save port information"
                return render_template('Companion/dberror.html', error=error)

    # Build static variables

    description = "Symetrical Link Aggregation for DL attached servers"
    test=[]
    port_counter = 1
    # Process a-side-ports
    while port_counter <= count:
        a_switch_ports = Ports.objects(silkscreen=str(port_counter))
        port_counter=port_counter + 1
        a_silkscreen=a_switch_ports[0]['silkscreen'].encode('utf-8')
        a_port_uuid=a_switch_ports[0]['uuid'].encode('utf-8')
        speed=a_switch_ports[0]['speed'].encode('utf-8')
        speed=int(speed)
        #
        # Find matching B side port    rick.append('fail')
        b_switch_ports = b_Ports.objects(silkscreen=a_silkscreen)
        for obj in b_switch_ports:
            if obj['switch_uuid'] == b_switch:
                b_port_uuid=obj['uuid'].encode('utf-8')
                b_port_silk=obj['silkscreen'].encode('utf-8')
        out = [a_silkscreen,b_port_silk,speed,a_port_uuid, b_port_uuid,port_counter, count]


        print 'writing lag to cfm....'
        name = "Auto generated link aggregation-%s" % (port_counter)
        result = fabric.add_lags(client, name, description, vlan_uuid, a_port_uuid, b_port_uuid, speed)
        test.append(out)
        print test

    return render_template('lags/autolag_success.html', result=result)


    #rick.append('fail')


    @lag_app.route('/testports', methods=('GET', 'POST'))
    def testports():

        # Process a-side-ports
        a_switch_ports = Ports.objects(switch_uuid=a_switch)
        for i in sorted (silkscreen.keys()):
            print i
        return render_template('lags/autolag_success.html')
