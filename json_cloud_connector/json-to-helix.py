import json
import requests
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--apikey', help='api Key - REQUIRED', required=True)
    parser.add_argument('--data', help='data you want to send to Helix , OPTIONAL', required=False)
    args, unknown = parser.parse_known_args()
    
    #default helix URL for the JSON Cloud Connector
    host = "https://helix-integrations.cloud.aws.apps.fireeye.com/api/upload"

    #headers for authentication to Helix
    headers = {"Authorization": args.apikey}

    #checks if the --data flag is used
    if args.data:
        logs = args.data
    else:
        log = {
            "class": "testing",
            "rawmsg": "this is a test",
            "hostname": "testing123",
            "srcipv4": "127.0.0.1"
        }

    #sends the log to Helix
    session = requests.Session()
    post_response = session.post(host, headers=headers, data=json.dumps(log))
    print(post_response)
    print(post_response.content)

if __name__ == "__main__":
    main()
