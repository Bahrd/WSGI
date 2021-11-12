##  https://en.wikipedia.org/wiki/Web_Server_Gateway_Interface

import requests
import json

def invoke(url, data):
    print('Sent-to a server: ' + json.dumps(data, indent = 0b11))
    # Invoke a service via POST...
    answer = requests.post(url, json = data).content
    # ... and wait for a response
    return json.loads(answer)

# A target "namespace" and       a function name... 
url = 'http://localhost:8006/' + 'Freddy2Jason'
# ... and its arguments 
data = {'ID':       0b1010, 
        'sender':   'Train Driver',
        'receiver': 'Traffic Controller',
        'message':  'Python Derailed',
        'severity': 3.141592653589793238462643,
        'flag':     True}

# They used to call the following 'a «stub»'
Freddy2Jason = lambda data: invoke(url = url, data = data)
# ... so that one can call a remote procedure as if it is local...
answer = Freddy2Jason(data)
print('Reply-from a server: ', json.dumps(answer, indent = 0b11))