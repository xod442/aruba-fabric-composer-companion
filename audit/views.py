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

# Place to stach the user temporarily
from database.companion import Companion
from pyhpecfm import fabric
from pyhpecfm import system
from utilities.get_client import access_client

audit_app=Blueprint('audit_app', __name__)

@audit_app.route('/view_alarms', methods=('GET', 'POST'))
def view_alarms():

    # Get a client connection.
    client=access_client()

    try:
        cfm_audits=system.get_audit_logs(client)
    except:
        error="ERR-LOGIN - Failed to log into CFM controller"
        return error

    # Create a empty list for alarms
    alarm_data=[]

    # Loop through cfm_audits and process ALARMS

    for alarm in cfm_audits:
        typex=alarm['record_type']
        if typex == 'ALARM':
            # Build dictionary to add to list
            out=[alarm['data']['event_type'],alarm['record_type'],alarm['severity'],alarm['description']]
            alarm_data.append(out)

    return render_template('audits/alarms.html', a=alarm_data)

@audit_app.route('/view_events', methods=('GET', 'POST'))
def view_events():

    # Get a client connection.
    client=access_client()

    try:
        cfm_audits=system.get_audit_logs(client)
    except:
        error="ERR-LOGIN - Failed to log into CFM controller"
        return error

    # Create a empty list for EVENTS
    event_data=[]

    # Loop through cfm_audits and process EVENTS
    for event in cfm_audits:
        typex=event['record_type']
        if typex == 'EVENT':
            # Build dictionary to add to list
            out=[event['description'],event['data']['event_type'],event['data']['object_name'],event['severity'],event['data']['event_type'],event['record_type']]
            event_data.append(out)

    return render_template('audits/events.html', e=event_data)
