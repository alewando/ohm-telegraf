#!/usr/bin/env python3

# Reads sensor data published to WMI by OpenHardwareMonitor and outputs it in influxdb line format
# Published metrics include tags for host, sensor id, sensor name, sensor type, sensor parent, and index (ie: CPU #2)

# Intended to be used as an external input in telegraf, which will feed the data to an influx db instance
# Example telegraf config:
# [[inputs.exec]]
#   interval = "60s"
#   commands = ['C:\\Path_To\\Python\\Python37\\python "c:\\Program Files\\telegraf\\ohm.py"']
#   data_format = "influx"

import wmi
import socket

hostname=socket.gethostname()

def esc(val): 
    return val.replace(' ','\ ')


w = wmi.WMI(namespace="root\OpenHardwareMonitor")
temperature_infos = w.Sensor()
for sensor in temperature_infos:
    #print(sensor)
    # if sensor.SensorType==u'Temperature':
    #     print(sensor.Name)
    #     print(sensor.Value)
    # else:
    #     print("Unknown Sensor " + str(sensor))
    print(f'OhmSensors,host={hostname},id="{esc(sensor.Identifier)}",name="{esc(sensor.Name)}",type="{esc(sensor.SensorType)}",parent="{esc(sensor.Parent)}",index={sensor.Index} value={sensor.Value}')