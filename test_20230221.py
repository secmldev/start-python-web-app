from flask import Flask

myapp = Flask(__name__)

@myapp.route("/")
def hello():
    return "I am happy to say hello"

@myapp.route("/mukund")
def greet():
    return "ok"

@myapp.route("/ishita")
def welcome():
    return "I am happy to say hello"

@myapp.route("/<name>")
def namaste(name):
    return "hello, sir " + name

@myapp.route("/<name>/<city>")
def my_client(name, city):
    return "hello, sir " + name + "when did you come from " + city



if __name__ == "__main__":
    myapp.run(debug=True)
