TOR IP Collector

This script is designed to collect tor IPs from the SecOps Institute master node list: https://raw.githubusercontent.com/SecOps-Institute/Tor-IP-Addresses/master/tor-nodes.lst


Required Flags:
--host <helix url>
  Description: This flag is used to set which cloud Helix instance to reach out to
  https://apps.fireeye.com/helix/id/<helix_id>
  
--apikey <api-key>
  Description: This flag is used to pass your Helix api-key for authenticating into Helix.
  
--listid <helix_list_id>
  Description: This flag is used to set which list the script will be posting the TOR IPs into
  
Optional Flags:
--ipv4 <>
  Description: Set if you only want IPv4 IPs in the Helix list
  Note: if you do not provide a ipv4, or ipv6 flag, the default will be to collect both. 
  
--ipv6
  Description: Set if you only want IPv6 IPs in the Helix list
  Note: if you do not provide a ipv4, or ipv6 flag, the default will be to collect both. 
