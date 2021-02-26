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

from flask import Flask
from flask_mongoengine import MongoEngine

db = MongoEngine()

def create_app(**config_overrides):
    app=Flask(__name__)
    app.config.from_pyfile('settings.py')

    app.config['MONGODB_SETTINGS'] = {
        'db': 'app_db',
        'host': 'localhost',
        'port': 27017,
        'username': 'appUser',
        'password': 'passwordForAppUser',
        'authentication_source': 'admin'
        }

    app.config.update(config_overrides)

    db.init_app(app)

    from main.views import main_app
    app.register_blueprint(main_app)

    from companion.views import companion_app
    app.register_blueprint(companion_app)

    from audit.views import audit_app
    app.register_blueprint(audit_app)

    from lags.views import lag_app
    app.register_blueprint(lag_app)

    from snmp.views import snmp_app
    app.register_blueprint(snmp_app)

    return app
