from flask import Flask, request
import json
app = Flask(__name__)

@app.route("/", methods = ['POST'])
def pingpong():
    print (request.json)
    return json.dumps(request.json)

if __name__ ==  '__main__':
    app.run(host='0.0.0.0' ,
            port=5000,
            debug=True)
