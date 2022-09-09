"""
Draft #1:
----------
Using Flask to handle HTTP requests

"""
from flask import Flask, request
from requests import get

app = Flask(__name__)

@app.route('/', defaults={'path': ''})

@app.route('/<path:path>')
def proxy(path):
#This allows for something like this url: http://127.0.0.1:5000/?host=https://XXX.com to return the content of whatever page is being asked for
    SITE_NAME = 'http://127.0.0.1:8000/'
    resp = get(f'{SITE_NAME}{path}').content
    print(request.url)
    return resp

#runs the app without having to set any of the env vars that are listed in the documentation
if __name__ == '__main__':
    app.run(debug=True)







