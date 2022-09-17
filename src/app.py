import socket
from unicodedata import name
from flask import Flask, jsonify, render_template
app = Flask(__name__)

def fetchDetails():
    hostname = socket.gethostname()
    hostip = socket.gethostbyname(hostname)
    return str(hostname), str(hostip)

@app.route("/details")
def hello_world():
    hostname, ip = fetchDetails()
    return f"<h1>Host name {hostname} & Host machine Ip is {ip} </h1>"

@app.route("/health")
def health():
    return jsonify(
        status="UP"
    )

@app.route("/")
def details():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)