# import the Flask class from the flask module
from flask import Flask, redirect, render_template
from web3 import Web3
from flask import send_file
import requests
from flask import url_for
# create the application object
app = Flask(__name__)


@app.route('/')
def cryptokraken():
    return render_template('cryptokraken.html')  # render a template


@app.route('/bobblemutants')
def bobblemutants():
    return render_template('bobblemutants.html')  # render a template


@app.route('/verify', methods=["GET", "POST"])
def verify():
    url = "https://polygon-mainnet.g.alchemy.com/v2/hTHbdkUCcWGAlUz69jYh8ex5mYKahsl6/getNFTs/?owner=0x5651A9DB991A71b1adC7253f57E61db56CBcc34C&contractAddresses[]=0x2953399124F0cBB46d2CbACD8A89cF0599974963&contractAddresses[]=0x2953399124F0cBB46d2CbACD8A89cF0599974963"
    output = "Generated Metadata:{backgrounds :yellow, head : darkblue, body  :  normal,  headgear: witch-hat, eyewear : thug, accessory : red-bowtie }"
    verify = requests.get(url)
    return output


@app.route('/download', methods=["GET"])
def download():
    return redirect(url_for('static', filename='images/nft.png'))


# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)
