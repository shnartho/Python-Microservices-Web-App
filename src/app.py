import socket
from unicodedata import name
from flask import Flask, jsonify, render_template
app = Flask(__name__)

def fetchDetails():
    hostname = socket.gethostname()
    hostip = socket.gethostbyname(hostname)
    return str(hostname), str(hostip)

@app.route("/")
def hello_world():
    return "<h1>Hi, Host machine Ip http://192.168.8.103 and Docker ip 192.168.59.101</h1>"

@app.route("/health")
def health():
    return jsonify(
        status="UP"
    )

@app.route("/detailss")
def detailss():
    hostname, ip = fetchDetails()
    return render_template('index.html', Hostname = hostname, Ip = ip)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)