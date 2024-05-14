from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World"

@app.route('/hello')
def hello():
    return "<h1>This is the first application. It says hello world.</h1>"


# Dynamic URLs
# URL Processor Examples
@app.route('/greet/<name>')
def greet(name):
    return f"Hello {name}! You are an amazing Python and Machine Learning Developer"


@app.route('/add/<int:number1>/<int:number2>')
def add(number1, number2):
    return f"The sum of {number1} and {number2} is {number1 + number2}"
    
# URL Paramenter Handling
# Reference: To use the parameter handling use this format: /handle_url_params?name=Hector&greeting=Hello
@app.route('/handle_url_params')
def handle_params():
    if 'greeting' in request.args.keys() and 'name' in request.args.keys():
        greeting = request.args['greeting']
        name = request.args.get('name')
        return f'{greeting}, {name}'
    else:
        return 'Some of the parameters are missing'


# Understanding GET and POST
# By default, GET is the method used when none is specified. 
@app.route('/hola', methods=['GET', 'POST']) # This statement supports both GET and POST. If the method is not specified GET is the default.
def hola():
    return f"Hello World using the methods GET and POST" 

# Example of using the GET and the POST by checking the method with - request.method 
# curl -X POST http://127.0.0.1:5510/getpost
# curl -X GET http://127.0.0.1:5510/getpost
@app.route('/getpost', methods=['GET', 'POST'])
def getpost():
    if request.method == 'GET':
        return 'You made a GET request\n'
    elif request.method == 'POST':
        return 'You made ap POST request\n'
    else:
        return 'You will never see this message\n' # This statement is never executed because no method is specified.


# Custom Responses
# Status Check using the -I and the make_response library imported at the top.
# curl -I http://127.0.0.1:5510/status
@app.route('/status')
def status():
    response = make_response('This is the status function.')
    response.status_code = 202
    response.headers['content-type'] = 'text/plain'
    return response
    







if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5510, debug=True)
    