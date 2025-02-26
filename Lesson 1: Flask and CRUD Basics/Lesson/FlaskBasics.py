from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Flask App!"

@app.route('/greet')
def greet():
    return "Welcome to Flask Robert"

@app.route('/greet/<username>')
def greetPersonal(username):
    return f"Welcome to Flask {username}"

if __name__ == '__main__':
    app.run(debug=True)
