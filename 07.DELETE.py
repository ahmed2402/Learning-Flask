# from flask import Flask

# app = Flask(__name__)

# @app.route('/api/users/<int:user_id>', methods = ['DELETE'])
# def delete_user(user_id):
#     return f"Deleting user with ID: {user_id}"

# app.run()

from flask import Flask, jsonify

app = Flask(__name__)  

users = [
    {'id': 1, 'name': "ahmed"},
    {'id': 2, 'name': "ali"},
    {'id': 3, 'name': "raza"},
]

@app.route('/api/users/<int:user_id>', methods = ['DELETE'])
def delete_user(user_id):
    for user in users:
        if user['id'] == user_id:
            users.remove(user)
            print(users)
            return jsonify({'message': 'User deleted successfully'})
    return jsonify({'message': 'User not found'}), 404

if __name__ == '__main__':
    app.run()    