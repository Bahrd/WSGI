##  https://en.wikipedia.org/wiki/Web_Server_Gateway_Interface

import requests
import json

def invoke(url, data):
    print('Sent-to a server: ' + json.dumps(data, indent = 3))
    answer = requests.post(url, json = data).content
    return_value = json.loads(answer)
    return return_value
# A target "namespace" and       a function name... 
url = 'http://localhost:8006/' + 'Freddy2Jason'

# They used to call it a 'stub'
Freddy2Jason = lambda data: invoke(url = url, data = data)

# ... and its arguments 
data = {'ID':       0b1010, 
        'sender':   'Train Driver',
        'receiver': 'Traffic Controller',
        'action':   'Python On Rails',
        'severity': 3.141592653589793238462643,
        'flag':     True}
## Invoke a service and wait... for a response
print('Reply-from a server: ', Freddy2Jason(data))