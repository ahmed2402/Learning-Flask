from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 123:
            return f"Welcome {username}"
        else:
            return "Invalid username or password"
    else:
        return render_template('login.html')

if __name__ == '__main__':
    app.run()

