# import the Flask class from the flask module
from flask import Flask, render_template

# create the application object
app = Flask(__name__)


@app.route('/')
def cryptokraken():
    return render_template('cryptokraken.html')  # render a template


@app.route('/bobblemutants')
def bobblemutants():
    return render_template('bobblemutants.html')  # render a template


# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)
