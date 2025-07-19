# from flask import Flask, jsonify

# app = Flask(__name__)

# @app.route('/api/users/<int:user_id>', methods=['PUT'])
# def update_user(user_id):
#     return f"Updating user with ID: {user_id}"

# if __name__ == '__main__':
#     app.run()


from flask import Flask, request, jsonify, Response

app = Flask(__name__)

users = [
    {'id': 1, 'name': 'John Doe'},
    {'id': 2, 'name': 'Jane Smith'}
]

@app.route('/api/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    for user in users:
        if user['id'] == user_id:
            user['name'] = data['name']
            return jsonify(user)
    return jsonify({'message': 'User not found'}), 404

if __name__ == '__main__':
    app.run()

# from flask import Flask, request, jsonify

# app = Flask(__name__)

# @app.route('/api/users/<id>', methods=['PUT'])
# def update_user(id):
#     data = request.json
#     name = data['name']
#     email = data['email']
#     user = {'id': id, 'name': name, 'email': email}
#     return jsonify(user)

# if __name__ == '__main__':
#     app.run()