import json
import urllib.request

import sys
import csv
import os

def request(action, **params):
    return {'action': action, 'params': params, 'version': 6}

def invoke(action, **params):
    requestJson = json.dumps(request(action, **params)).encode('utf-8')
    response = json.load(urllib.request.urlopen(urllib.request.Request('http://127.0.0.1:8765', requestJson)))
    if len(response) != 2:
        raise Exception('response has an unexpected number of fields')
    if 'error' not in response:
        raise Exception('response is missing required error field')
    if 'result' not in response:
        raise Exception('response is missing required result field')
    if response['error'] is not None:
        raise Exception(response['error'])
    return response['result']

# Check command line inputs
def main():

    target_file = os.path.abspath(f"{sys.argv[1]}")
    target_file = target_file.replace("\\","/")
    invoke("guiImportFile", path = target_file)

if __name__ == '__main__':
    main()
