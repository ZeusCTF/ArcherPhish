"""
Draft #1:
----------
Using Flask to handle HTTP requests

"""
import socket
from flask import Flask, request

app = Flask(__name__)

def proxyHandle(path):
    host = request.headers.get('Host')
    method = request.method
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((f"{host}",80))
    req = f"{method} /{path} HTTP/1.1\r\nHost: {host}\r\n\r\n"
    s.sendall(str.encode(req))
    resp = s.recv(4096)
    s.close
    return resp
    


#reqPath functions as a dynamic var that allows any page to be requested
#instead of the alternative of creating a route for every single page that could be on a remote site
@app.route("/<reqPath>", methods=['GET','POST'])
def render(reqPath):
    return proxyHandle(reqPath)
    

@app.route('/')
def main():
    print(request.headers)
    return "main page"

#runs the app without having to set any of the env vars that are listed in the documentation
if __name__ == '__main__':
    app.run(debug=True)







