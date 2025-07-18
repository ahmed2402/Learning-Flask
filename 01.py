from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello, Nigga!</h1>"

@app.route('/class')
def classs():
    return "<h1>Hello, Class!</h1>"

@app.route('/class/<int:id>')
def myclass(id):
    return f"<h1>Hello, {id}!</h1>"

@app.route('/appname')
def appname():
    return "<h1>Application name:--> {}</h1>".format(__name__)


if __name__ == '__main__':
    app.run()
