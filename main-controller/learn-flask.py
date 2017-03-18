# SIMPLE ROUTE
@app.route("/")
def hello():
    # somestuff
    print("SIMPLE ROUTE")


# RECIEVING POST REQUEST
@app.route('/post', methods=['POST'])
def resultp():
    # print(request.form['foo'])  # should display 'bar'
    print(request.form.getlist('data[]'))  # should display 'bar'
    return json.dumps(["Recieved!"])


# RECIEVING GET REQUEST
@app.route('/get', methods=['GET'])
def result():
    # print(request.form['foo'])  # should display 'bar'
    pprint.pprint(request.args)  # should display 'bar'
    return 'Received !'  # response to your request.


# SENDING A POST REQUEST
r = requests.post("http://httpbin.org/post", data={'foo': 'bar'})
print(r.text)
