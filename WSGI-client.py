##  https://en.wikipedia.org/wiki/Web_Server_Gateway_Interface

import requests
import json

def invoke(url, data):
    print('Sent-to a server: ' + json.dumps(data, indent = 0b11))
    # Invoke a service via POST...
    rpc = requests.post(url, json = data)
    answer = rpc.content
    # ... and wait for a response
    return json.loads(answer)

# A target "namespace" and       a function name... 
url = 'http://localhost:8006/' + 'Freddy2Jason'
# ... and its arguments 
params = {'ID':       0b1010, 
          'sender':   'Train Driver',
          'receiver': 'Traffic Controller',
          'message':  'Python Derailed',
          'severity': 3.141592653589793238462643,
          'code':     'a, b, c = 32, 33, 34; code = a * (b + c)',
          'flag':     True}

# They used to call the following 'a «stub»'
Freddy2Jason = lambda data: invoke(url = url, data = data)
# ... so that one can call a remote procedure as if it is local...
answer = Freddy2Jason(params)
print('Reply-from a server: ', json.dumps(answer, indent = 0b11))
