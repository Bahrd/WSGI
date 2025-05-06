##  https://en.wikipedia.org/wiki/Web_Server_Gateway_Interface
from flask import Flask, request
import json

app = Flask(__name__)
@app.route('/RPC', methods = ['POST'])
def RPC():
    args = request.json
    print('RAW request', request, args)
    
    # Sometimes servers gotta do what the servers gotta do...
    args['ID'], args['message'] = 0o52, '¡Python On Rails!'
 
    print('Reply-to a client: ', json.dumps(args, indent = 0b11, ensure_ascii = False).encode('utf8').decode())
    # ... and send a result back to a client
    return args

if __name__ == '__main__':
    app.run(host = 'localhost', port = '8006', debug = True)