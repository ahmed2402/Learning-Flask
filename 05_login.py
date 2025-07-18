# from flask import Flask, request, render_template

# # Create a Flask application instance
# app = Flask(__name__)

# # Define a route for '/formlogin' that accepts both GET and POST requests
# @app.route("/formlogin", methods=['GET', 'POST'])
# def login():
#     # Check if the request method is POST (i.e., form was submitted)
#     if request.method == "POST":
#         uname = request.form['username']
#         password = request.form['user_password']
#         if uname == "admin" and password == "123":
#             return "Welcome " + uname
#         else:
#             return "Try again"
#     else:
#         # If the request method is GET, render the login form template
#         return render_template('login.html')

# # Run the Flask application if this script is executed directly
# if __name__ == '__main__':
#     app.run()

from flask import Flask, request, render_template

app = Flask(__name__)

@app.get("/formlogin")
def login():
    return render_template('login.html')
    print("Runing.........")
    uname = request.form['uname']
    password = request.form['password']
    print(uname,password)
    if uname == "admin" and password == "123":
        return "Welcome " + uname
    else:
        return "Try again"

if __name__ == '__main__':
    app.run()