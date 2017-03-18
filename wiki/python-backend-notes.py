import requests
from flask import Flask, request, jsonify
from flask_cors import CORS
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop

requestCount = 0
app = Flask(__name__)
CORS(app)
# SENDING A POST REQUEST
r = requests.post("http://httpbin.org/post", data={'foo': 'bar'})
print(r.text)


# RECIEVING POST REQUEST
@app.route('/post', methods=['POST'])
def result():
    print(request.form['foo'])  # should display 'bar'
    return 'Received !'  # response to your request.


# SIMPLE ROUTE
@app.route("/")
def hello():
    global requestCount
    requestCount += 1
    return jsonify(["Hello World! Backend recieved " + str(requestCount) + " requests."])


if __name__ == "__main__":
    http_server = HTTPServer(WSGIContainer(app))
    http_server.listen(5000)
    IOLoop.instance().start()

#===========================================================
#TO READ SETTINGS FROM INI
