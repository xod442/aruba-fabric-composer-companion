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

from flask import Blueprint, render_template, request, redirect, session, url_for, abort
import os
# from werkzeug import secure_filename
from mongoengine import Q
import pygal
import json

# Place to stach the user temporarily
from database.temp import Temp
from database.companion import Companion
from database.ports import Ports
from database.number import Number
from database.switches import Switches
from pyhpecfm.client import CFMClient
from pyhpecfm import fabric
from utilities.switch_array import get_switches
from utilities.get_charts import build_charts

main_app=Blueprint('main_app', __name__)

@main_app.route('/main', methods=('GET', 'POST'))
@main_app.route('/', methods=('GET', 'POST'))
@main_app.route('/index', methods=('GET', 'POST'))
def main():
    ''' Delete any residual links in the db and display the main menu
    '''
    # Clear switches database on new session.
    Switches.objects().delete()

    # Clear switches database on new session.
    Ports.objects().delete()


    return render_template('main/main.html')

@main_app.route('/help', methods=('GET', 'POST'))
def help():

    return render_template('main/help.html')

@main_app.route('/main_select', methods=('GET', 'POST'))
def main_select():
    #import cfm_api_utils as c
    ipaddress=request.form['ipaddress']
    user=request.form['user']
    passwd=request.form['passwd']

    # Authenticat to the controller
    client=CFMClient(ipaddress,user,passwd)
    client.connect()

    # Build database entry to save creds
    creds = Companion(user=user,passwd=passwd,ipaddress=ipaddress)
    # Save the record
    try:
        creds.save()
    except:
        error="ERR001 - Failed to save login credentials"
        return render_template('companion/dberror.html', error=error)

    '''
    # Turn on to build num db on initial run
    number = 1
    num = Number(num=number)
    try:
        num.save()
    except:
        error = "ERR999 - Could not create number database"
        return render_template('companion/dberror.html', error=error)
    '''

    # Returns a list a auto generated charts
    charts=build_charts()

    # Get the switches from the controller and save to the mongo database
    try:
        switches=fabric.get_switches(client)
    except:
        error="ERR-LOGIN - Failed to log into CFM controller"
        return render_template('companion/dberror.html', error=error)

    switch_data=[]
    # Process switch datat from plexxi API
    for switch in switches:
        health=switch['health']['status']
        ip_address=switch['ip_address']
        mac_address=switch['mac_address']
        name=switch['name']
        sw_version=switch['sw_version']
        uuid=switch['uuid']
        model=switch['model']
        role=switch['role']

        #

        # Write to switches database
        switch_info=Switches(health=health,ip_address=ip_address, mac_address=mac_address, name=name, sw_version=sw_version, uuid=uuid, model=model, role=role)
        # rick.append('fail')
        # Save the record
        try:
            switch_info.save()
        except:
            error="ERR001X - Failed to save switch information"
            return render_template('companion/dberror.html', error=error)

        # Build list to write out to user interface
        out=[health,ip_address,mac_address,name,sw_version,model,role]
        switch_data.append(out)

    return render_template('main/companion1.html',u=user,i=ipaddress,g1_data=charts[0],g2_data=charts[1],s=switch_data)


@main_app.route('/main_return', methods=('GET', 'POST'))
def main_return():
    # Get user informaation
    creds = Companion.objects.first()
    user = creds.user
    ipaddress= creds.ipaddress

    # Insert chart data
    charts=build_charts()

    # Get switch information switch database
    switch_array=get_switches()

    return render_template('main/companion1.html',u=user,i=ipaddress,g1_data=charts[0],g2_data=charts[1],s=switch_array)

@main_app.route('/main_logout', methods=('GET', 'POST'))
def main_logout():
    # Clear companion creds database for log information.
    Companion.objects().delete()
    # Dump the switches database
    Switches.objects().delete()

    return render_template('main/logout.html')
