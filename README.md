Reads sensor data published to WMI by OpenHardwareMonitor and outputs it in influxdb line format.
Published metrics include tags for host, sensor id, sensor name, sensor type, sensor parent, and index (ie: CPU #2)

Intended to be used as an external input in telegraf, which will feed the data to an influx db instance
Example telegraf config:
```
[[inputs.exec]]
  interval = "60s"
  commands = ['C:\\Path_To\\Python\\Python37\\python "c:\\Program Files\\telegraf\\ohm.py"']
  data_format = "influx"
```
