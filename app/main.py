from flask import Flask
app = Flask(__name__)

#Normal nginx app to display welcome message
@app.route("/")
def hello():
    return "Hello it's XLR/XLD/K8 deployment with ingress host v 1.0"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
