#!/usr/bin/env python
import httplib
import json
import sys

MINIMUM_CHARACTERS = 5
LODGEIT_SERVER = 'paste.adku.com'
LODGEIT_API_JSON_PATH = '/json/?method=pastes.newPaste'

data_from_stdin = sys.stdin.read()
if not data_from_stdin or len(data_from_stdin) < MINIMUM_CHARACTERS:
    print 'No data on stdin, at least %d character(s) required' % MINIMUM_CHARACTERS
    sys.exit(1)

headers = {
    'Content-Type': 'application/json'
}

paste_contents = {
    'language': None,
    'code': data_from_stdin
}
jsoned_paste_request = json.dumps(paste_contents)

paste_connection = httplib.HTTPConnection(LODGEIT_SERVER)
paste_connection.request("GET", LODGEIT_API_JSON_PATH, body=jsoned_paste_request, headers=headers)
paste_response = paste_connection.getresponse()
response_body = paste_response.read()
paste_connection.close()

response_data = json.loads(response_body)

print ""
print "http://%(host)s/show/%(paste)s/" % dict(host=LODGEIT_SERVER, paste=response_data['data'])
