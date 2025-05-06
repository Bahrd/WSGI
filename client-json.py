##  https://en.wikipedia.org/wiki/Web_Server_Gateway_Interface

import requests
import json

def invoke(url, args):
    print('Sent-to a server:', json.dumps(args, indent = 0b11, ensure_ascii = False).encode().decode())
          
    # Invoke a service via POST...
    rpc = requests.post(url, json = args)
    answer = rpc.content
    # ... and wait for a response
    return json.loads(answer)

#     A target "namespace",       a function name... 
url = 'http://localhost:8006/' + 'RPC'
# ... and its arguments 
args = {
          'ID':       0b1010, 
          'message':  '¿Python Derailed?', 
       }

for _ in range(20):
    answer = invoke(url = url, args = args)
    print('Reply-from a server: ', json.dumps(answer, indent = 0b11, ensure_ascii = False).encode().decode())