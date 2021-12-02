# JSON-to-Helix

This simple script is designed to be the framework of sending custom JSON data into Helix as an event. 
Instead of using the curl command example FireEye provides, you can utilize this script to create custom Helix events with Python

The API Key and JSON data are simply passed through as an argument directly to the 'requests' library. 

## Flags

### --apikey
Pass the API Key Helix automatically generates for you when you install the JSON Cloud Connector

### --data
Pass the JSON data you want to send to Helix. Use the JSON Cloud Connector install steps to view a comprehensive list of all available Helix fields. 
Example: --data {"class": "testing", "rawmsg": "this is a test", "hostname": "testing123", "srcipv4": "127.0.0.1"}
