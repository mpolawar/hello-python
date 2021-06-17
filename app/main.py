from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello it's XLR/XLD/K8 deployment test for version 2.0.0"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
