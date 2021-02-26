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

from flask_wtf import Form
from wtforms import validators, StringField, PasswordField, BooleanField, SelectField, TextAreaField
from wtforms.widgets import TextArea
from wtforms.fields.html5 import EmailField
from wtforms.validators import ValidationError
from flask_wtf.file import FileField, FileAllowed
import re

from database.models import Database

class DatabaseForm(Form):
    user = StringField('System User', [validators.DataRequired()])
    now = StringField('Time Stamp', [validators.DataRequired()])
    num = StringField('Number', [validators.DataRequired()])
    message = StringField('Entry Body', [validators.DataRequired()], render_kw={"rows": 5, "cols": 65})
    concern = StringField('Concerns/Issues', [validators.DataRequired()], render_kw={"rows": 5, "cols": 65})
