from flask import Flask, request
import json
import mysql.connector
app = Flask(__name__)

@app.route("/", methods = ['POST'])
def pingpong():
    print (request.json)
    return json.dumps(request.json)

@app.route("/busca", methods = ['POST'])
def busca():
    req = request.json
    cnx = mysql.connector(user='',
                          password='',
                          database='',
                          host='localhost')
    cursor = cnx.cursor()
    resultado = cursor.execute('select *
                               from ingrediente
                               where produto =
                               (select id from produto where nome = "alho")')
    print (resultado)
    cursor.close()
    cnx.close()
    return resultado


if __name__ ==  '__main__':
    app.run(host='0.0.0.0' ,
            port=5000,
            debug=True)
