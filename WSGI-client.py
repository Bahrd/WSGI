##  https://en.wikipedia.org/wiki/Web_Server_Gateway_Interface

import requests
import json

def invoke(url, args):
    print('Sent-to a server: ' + json.dumps(args, indent = 0b11))
    # Invoke a service via POST...
    rpc = requests.post(url, json = args)
    answer = rpc.content
    # ... and wait for a response
    return json.loads(answer)

#     A target "namespace" and a "function" name... 
url = 'http://localhost:8006/' + 'Freddy0b10Jason'
# ... and its arguments 
args = {
          'ID':       0b1010, 
          'message':  'Python Derailed',
          'severity': 3.141592653589793238462643,
          # Note that we send a Python snippet to be [exe|electro]-cuted by a server.
          'code':     'from numpy import sqrt; α, β, γ = 0o10, 0x10, 0b10; code = sqrt(α * (β + γ))'
          # Not a good practise (from either server's performance or security vantage point), 
          # however...
       }

# They used to call the following 'a «stub»' (i.e. a client-side wrapper of a remote procedure)
Freddy2Jason = lambda args: invoke(url = url, args = args)

# ... so that one can call a remote procedure as if it is local...
answer = Freddy2Jason(args)
print('Reply-from a server: ', json.dumps(answer, indent = 0b11))
