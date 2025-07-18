#this method won't work as this method is not allowed in the browser
# from flask import Flask, jsonify

# app = Flask(__name__)

# @app.route('/api/users', methods=['POST'])
# def create_user():
#     return 'Creating a new user'

# if __name__ == '__main__':
#     app.run()


#use this instead
# from flask import Flask, jsonify

# app = Flask(__name__)

# @app.route('/api/users', methods=['POST'])
# def create_user():
#     return jsonify({"message": "Creating a new user"})

# if __name__ == '__main__':
#     app.run()


# from flask import Flask, request

# app = Flask(__name__)

# @app.route('/api/users', methods=['POST'])
# def create_user():
#     data = request.json
#     name = data.get('name')
#     return f"Creating a new user: {name}"

# if __name__ == '__main__':
#     app.run()


# from flask import Flask, request, jsonify

# app = Flask(__name__)

# users = []

# # @app.route('/api/users', methods=['POST'])
# @app.post('/api/users')
# def create_user():
#     data = request.json
#     name = data.get('name')
#     email = data.get('email')
#     new_user = {'name': name, 'email': email}
#     users.append(new_user)
#     return jsonify(new_user), 202

# if __name__ == '__main__':
#     app.run()


from flask import Flask, request, jsonify

app = Flask(__name__)

users = []

@app.route('/api/users', methods=['POST'])
def create_user():
    new_user = request.get_json()
    users.append(new_user)
    print(users)
    return jsonify(new_user), 201

@app.route('/api/users', methods=['GET'])
def get_users():
    return jsonify(users)

if __name__ == '__main__':
    app.run()


