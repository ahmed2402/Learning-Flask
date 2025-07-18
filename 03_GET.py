# from flask import Flask, jsonify

# app = Flask(__name__)

# users = [
#     {'id': 1, 'name': 'John Doe'},
#     {'id': 2, 'name': 'Jane Smith'}
# ]

# @app.route('/')
# def index():
#     return 'Hello, World!'

# @app.route('/api', methods=['GET', 'POST'])
# def get_users():
#     return jsonify(users)


# if __name__ == '__main__':
#     app.run(port=3000)

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def get_users():
    users = []
    users.append({'id': 1, 'name': 'John Doe'})
    users.append({'id': 2, 'name': 'Jane Smith'})
    users.append({'id': 3, 'name': 'Alice Johnson'})
    return jsonify({'users': users})

if __name__ == '__main__':
    app.run()

