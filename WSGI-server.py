##  https://en.wikipedia.org/wiki/Web_Server_Gateway_Interface

from flask import Flask, request, send_file
import json

app = Flask(__name__)
# 'Are you alive?'
@app.route('/')
def AYA():
    docs = 'https://pythonbasics.org/flask-rest-api/' 
    return f'Go for <a href ="{docs}">docu\'drama<a/>...'

# Request for a file with GET
@app.route('/apps/<converter>', methods = ['GET'])
def download_file(converter):
    return send_file('./WSGI-form.html', as_attachment = False)
# Request for an image GET
@app.route('/apps/SFP.JPEG', methods = ['GET'])
def download_image():
    return send_file('./San Francisco Peaks.JPEG', as_attachment = False)

# Request form with GET
@app.route('/converter')
def edge_form():
    value = request.args.get('MPG')
    mpg2lkm = 3.78541178/1.609344 * 100 #gallon/mile * km
    return 'Gotcha {:.3}l/100km!'.format(mpg2lkm/eval(value))

# Web service with POST & JSON
@app.route('/Freddy0b10Jason', methods = ['POST'])
def JSNX():
    args = request.json
    print('RAW request', request, args)
    
    # Sometimes servers gotta do what the servers gotta do...
    args['ID'], args['severity'], args['message'] = 0o52, 2.718281828459045, 'Python On Rails'

    # https://stackoverflow.com/questions/37237034/how-to-get-results-out-of-a-python-exec-eval-call
    command, aux = args['code'], {}
    exec(command, aux)
    args['code'] = str(aux['code'])
    
    print('Reply-to a client: ', json.dumps(args, indent = 0b11))
    # ... and send a result back to a client
    return args

## Run a server and wait... 
#               and wait... 
#               and wait... 
#  ... for a client's request
if __name__ == '__main__':
    app.run(host = 'localhost', port = '8006', debug = True)