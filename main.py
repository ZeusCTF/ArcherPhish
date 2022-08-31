"""
Draft #1:
----------
Using Flask to handle HTTP requests

"""
import re
from flask import Flask, request

app = Flask(__name__)

def proxyHandle():
    host = request.headers.get('Host')
    method = request.method




#reqPath functions as a dynamic var that allows any page to be requested
#instead of the alternative of creating a route for every single page that could be on a remote site
@app.route("/<reqPath>", methods=['GET','POST'])
def render(reqPath):
    proxyHandle()
    return "<h1>Hello World</h1>"

@app.route('/')
def main():
    print(request.headers)
    return "main page"

#runs the app without having to set any of the env vars that are listed in the documentation
if __name__ == '__main__':
    app.run(debug=True)







