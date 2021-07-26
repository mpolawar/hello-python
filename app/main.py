from flask import Flask
app = Flask(__name__)

#Normal nginx app to display welcome message
@app.route("/")
def hello():
    return "Hello it's application deployment demo on K8 using DAI Release/Deploy:  Version 1.0"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
