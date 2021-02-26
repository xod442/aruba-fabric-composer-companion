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
from pygal.style import LightGreenStyle

def build_charts():
    # Build some sample charts

    try:
        from pygal.style import DarkSolarizedStyle
        g1=pygal.StackedLine(fill=True, interpolate='cubic', style=DarkSolarizedStyle)
        g1.add('A', [1, 3,  5, 16, 13, 3,  7])
        g1.add('B', [5, 2,  3,  2,  5, 7, 17])
        g1.add('C', [6, 10, 9,  7,  3, 1,  0])
        g1.add('D', [2,  3, 5,  9, 12, 9,  5])
        g1.add('E', [7,  4, 2,  1,  2, 10, 0])
        g1_data=g1.render_data_uri()
    except Exception, e:
		return(str(e))

    try:
        line_chart=pygal.HorizontalBar()
        line_chart.title = 'Browser usage in February 2012 (in %)'
        line_chart.add('IE', 19.5)
        line_chart.add('Firefox', 36.6)
        line_chart.add('Chrome', 36.3)
        line_chart.add('Safari', 4.5)
        line_chart.add('Opera', 2.3)
        line_chart.render()
        g2_data=line_chart.render_data_uri()
    except Exception, e:
		return(str(e))

    charts=[g1_data,g2_data]

    return charts



    return switch_array
