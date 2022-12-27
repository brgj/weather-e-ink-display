# Importation of Python modules 
from datetime import datetime, timedelta
import re
import warnings

# The following modules must first be installed to use 
# this code out of Jupyter Notebook
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy
from owslib.wms import WebMapService
import pandas
from tabulate import tabulate

# Ignore warnings from the OWSLib module
warnings.filterwarnings('ignore', module='owslib', category=UserWarning)

# Parameters choice
# Layer:
# layer = 'HRDPS.CONTINENTAL_TT'
layer = 'CURRENT_CONDITIONS'
# Coordinates:
y, x = 45.481044, -73.587200
# Local time zone (in this exemple, the local time zone is UTC-05:00):
time_zone = -5

# bbox parameter
min_x, min_y, max_x, max_y = x - 0.25, y - 0.25, x + 0.25, y + 0.25


# WMS service connection
wms = WebMapService('https://geo.weather.gc.ca/geomet?SERVICE=WMS' +
                    '&REQUEST=GetCapabilities',
                    version='1.3.0',
                    timeout=300)
# Extraction of temporal information from metadata
# def time_parameters(layer):
#     start_time, end_time, interval = (wms[layer]
#                                       .dimensions['time']['values'][0]
#                                       .split('/')
#                                       )
#     iso_format = '%Y-%m-%dT%H:%M:%SZ'
#     start_time = datetime.strptime(start_time, iso_format)
#     end_time = datetime.strptime(end_time, iso_format)
#     interval = int(re.sub(r'\D', '', interval))
#     return start_time, end_time, interval


# start_time, end_time, interval = time_parameters(layer)

# To use specific starting and ending time, remove the #
# from the next lines and replace the start_time and
# end_time with the desired values:
# start_time = 'YYYY-MM-DDThh:00'
# end_time = 'YYYY-MM-DDThh:00'
# fmt = '%Y-%m-%dT%H:%M'
# start_time = datetime.strptime(start_time, fmt) - timedelta(hours=time_zone)
# end_time = datetime.strptime(end_time, fmt) - timedelta(hours=time_zone)

# Calculation of date and time for available predictions
# (the time variable represents time at UTC±00:00)
# time = [start_time]
# local_time = [start_time + timedelta(hours=time_zone)]
# while time[-1] < end_time:
    # time.append(time[-1] + timedelta(hours=interval))
    # local_time.append(time[-1] + timedelta(hours=time_zone))

# Loop to carry out the requests and extract the probabilities
def request(layer): 
    info = []
    pixel_value = []
    # for timestep in time:
    # WMS GetFeatureInfo query
    info.append(wms.getfeatureinfo(layers=[layer],
                                    srs='EPSG:4326',
                                    bbox=(min_x, min_y, max_x, max_y),
                                    size=(100, 100),
                                    format='image/jpeg',
                                    query_layers=[layer],
                                    info_format='text/plain',
                                    xy=(50, 50),
                                    feature_count=1
                                #    time=str(timestep.isoformat()) + 'Z'
                                    ))
    # Probability extraction from the request's results
    text = info[-1].read().decode('utf-8')
    print(text)
    pixel_value.append(str(re.findall(r'temp\s+\d*.*\d+', text)))
    pixel_value[-1] = (float(
        re.sub('temp = \'', '', pixel_value[-1])
        .strip('[""]')
    ))
    
    return pixel_value

pixel_value = request(layer)

print(pixel_value)