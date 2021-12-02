# TOR IP Collector

This script is designed to collect tor IPs from the SecOps Institute master node list: https://raw.githubusercontent.com/SecOps-Institute/Tor-IP-Addresses/master/tor-nodes.lst


## Flags:
### --host
  Description: This flag is used to set which cloud Helix instance will be reached out to
  
### --apikey
  Description: This flag is used to pass your Helix api-key for authenticating into Helix.
  
### --listid
  Description: This flag is used to set which list the script will be posting the TOR IPs into. Pass the ID of the list, not the list name
  
## Optional Flags:
### --ipv4
  Description: Set if you only want IPv4 IPs in the Helix list
  
### --ipv6
  Description: Set if you only want IPv6 IPs in the Helix list

#### Note: if you do not provide a ipv4, or ipv6 flag, the default will be to collect both. 
