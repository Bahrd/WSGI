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
@app.route('/Freddy2Jason', methods = ['POST'])
def JSNX():
    content = request.json
    print('RAW request', request, content)
    
    # Sometimes servers gotta do what the servers gotta do...
    content['ID'], content['severity'] = 0o52, 2.718281828459045
    content['receiver'], content['sender'] = content['sender'], content['receiver']
    content['message'] = 'Python On Rails'

    # https://stackoverflow.com/questions/37237034/how-to-get-results-out-of-a-python-exec-eval-call
    command, ret = content['code'], {}
    exec(command, ret)
    content['code'] = str(ret['code'])
    
    print('Reply-to a client: ', json.dumps(content, indent = 0b11))
    # ... and send a result back to a client
    return content

## Run a server and wait... 
#               and wait... 
#               and wait... 
#  ... for invocation
if __name__ == '__main__':
    app.run(host = 'localhost', port = '8006', debug = True)