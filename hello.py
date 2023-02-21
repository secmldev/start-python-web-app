from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello() -> str:
    return "Hello World"


@app.route('/nitin')
def welcome():
    return 'welcome Nitin, what is your order'

@app.route('/vishnu')
def greet():
    return 'Welcome Vishnu ji, what is your order'

@app.route('/hari')
def namaskar():
    return 'Welcome Hari ji, what is your order'

@app.route('/<name>')
def good_morning(name):
    return 'Welcome ' +  name +', what is your order'


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)