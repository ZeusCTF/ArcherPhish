from flask import Flask, request
import requests

app = Flask(__name__)
SITE_NAME = 'http://127.0.0.1:5000/'

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>', methods=['GET','POST'])
def proxy(path):
  if request.method == 'POST':
    print(request.form)
    print(request.cookies)
    requests.post(f'{SITE_NAME}', data=request.form)
  return requests.get(f'{SITE_NAME}{path}').content

if __name__ == '__main__':
  app.run(port=9001)