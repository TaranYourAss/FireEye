import requests
import argparse
import json
from datetime import date
import urllib.request
import ipaddress


#custom exception for if purging the Helix TOR IP list fails 
class DeleteListFailed(Exception):
    pass

#custom exception for if POSTing the updated list of TOR IPs into Helix fails
class PostListFailed(Exception):
    pass

#reaches out to the website and collects all TOR IPs
def pulldata (target_url, ip_type):
    ipv4_tor = []
    ipv6_tor = []
    for line in urllib.request.urlopen(target_url):
        line = line.decode()
        line = line.rstrip("\n")
        try:
            ipaddress.IPv4Address(line)
        except ValueError:
            try:
                ipaddress.IPv6Address(line)
            except ValueError:
                print("Unknown IP type")
                print(line)
            else:
                ipv6_tor.append(line)
        else:
            ipv4_tor.append(line)
    if (ip_type == "ipv4"):
        return ipv4_tor;
    elif (ip_type == "ipv6"):
        return ipv6_tor;

def main():
    parser = argparse.ArgumentParser()
    #parser.add_argument('--host', help='host , REQUIRED', required=True)
    parser.add_argument('--apikey', help='password , REQUIRED', required=True)
    args, unknown = parser.parse_known_args()
    #host = args.host.rstrip('/')

    #headers for authentication to Helix
    headers = {
        "x-fireeye-api-key": args.apikey,
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    #query to POST JSON disctionary list into Helix
    #import_list = "{}/api/v3/lists/{}/items/import".format(host, "592155")
    import_list = "https://apps.fireeye.com/helix/id/XXXXXX/api/v3/lists/XXXXX/items/import"

    #query to DELETE all items in the tor_ips list in Helix
    #delete_list = "{}/api/v3/lists/{}/items".format(host, "592155")
    delete_list = "https://apps.fireeye.com/helix/id/XXXXX/api/v3/lists/XXXXXX/items"

    #injects todays date into the notes for every TOR IP entry in Helix
    notes = "Added: " + str(date.today())

    session = requests.Session()
    json_data = []
    #--end of variables--

    #1 - Collect TOR IPs
    tor_ipv4 = pulldata(target_url='https://raw.githubusercontent.com/SecOps-Institute/Tor-IP-Addresses/master/tor-nodes.lst', ip_type="ipv4")
    tor_ipv4.sort()
    tor_ipv6 = pulldata(target_url='https://raw.githubusercontent.com/SecOps-Institute/Tor-IP-Addresses/master/tor-nodes.lst', ip_type="ipv6")
    tor_ipv6.sort()

    #2 - Purge list of IPs in Helix
    try:
        delete_response = session.delete(delete_list, headers=headers)
        if delete_response.status_code not in range(200, 300): 
            raise DeleteListFailed
    except DeleteListFailed:
        print("Deleting the tor_ips list failed")
        print(delete_response.status_code)
        exit(-1)

    #3 - Create list of JSON dictionaries from updated TOR IP list
    for ip in tor_ipv4:
        json_data.append({"value": ip, "type": "ipv4", "risk":"Medium", "notes":notes})
    for ip in tor_ipv6:
        json_data.append({"value": ip, "type": "ipv6", "risk":"Medium", "notes":notes})

    #4 - POST JSON data into Helix
    try:
        post_response = session.post(import_list, headers=headers, data=json.dumps(json_data))
        if post_response.status_code not in range(200, 300): 
            raise PostListFailed
    except PostListFailed:
        print("POSTing the tor_ips list failed")
        print(post_response)
        exit(-1)

if __name__ == "__main__":
	main()
    
#test_data = [{"value":"127.0.0.1","type":"ipv4","risk":"Medium","notes":""}, {"value":"127.0.0.2","type":"ipv4","risk":"Medium","notes":""}]

