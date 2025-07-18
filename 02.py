# import json
# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return json.dumps(  #.dumps() is used to convert the dictionary to a JSON string, it takes a dictionary and returns a JSON string
#         {
#             'name': 'John',
#             'age': 20,
#             'city': 'New York'
#         }
#     )

# app.run()

import json
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify( #jsonify() is used to convert the dictionary to a JSON string, it takes a dictionary and returns a JSON string  
        {
            'name': 'John',
            'age': 20,
            'city': 'London'
        }
    )

@app.route('/api/data')
def getdata():
    data = {
        'name' : 'Ahmed',
        'age' : 20,
        'city' : 'Karachi'
    }

    return jsonify(data)


@app.route("/calcu/<int:n>")
def calculate(n):
    result = {"Value":n**n,
             "Type":"int"}
    print(result)
    return jsonify(result)

@app.route("/name/<string:fname>")
def name(fname):
    result = {"Name":fname}
    return result

if __name__ == '__main__':
    app.run()

