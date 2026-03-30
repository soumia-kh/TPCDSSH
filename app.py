from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Application Flask déployée via CI/CD !</h1>'

if __name__ == '_main_':
    app.run(host='0.0.0.0', port=5000)