from flask import Flask, request, make_response, render_template

app = Flask(__name__, template_folder='templates')

# Note: the template folder is defined in the app statement. It doesn't need to be specified in the render_template
# Flask Tutorial Series #3 covers additional code examples: jinja, passing values to html, base.html, and dynamic filters.  
# Due to lack of time, I'm not re-creating the code inside the NeuralNine video #3. 
@app.route('/')
def index():
    return render_template('index.html') 


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5510, debug=True)
    