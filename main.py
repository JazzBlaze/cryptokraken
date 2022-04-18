# import the Flask class from the flask module
from flask import Flask, render_template
# from web3 import Web3
# Python: web3.py
# web3 = Web3(Web3.HTTPProvider(
#     "https://eth-mainnet.alchemyapi.io/v2/hTHbdkUCcWGAlUz69jYh8ex5mYKahsl6"))
# blocknumber = web3.eth.getBlockNumber()
# print(blocknumber)

# create the application object
app = Flask(__name__)


@app.route('/')
def cryptokraken():
    return render_template('cryptokraken.html')  # render a template


@app.route('/bobblemutants')
def bobblemutants():
    return render_template('bobblemutants.html')  # render a template

@app.route('/octarak')
def octarak():
    return render_template('octarak.html')  # render a template

@app.route('/nftspawn')
def nftspawn():
    return render_template('nftspawn.html')  # render a template


# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)
