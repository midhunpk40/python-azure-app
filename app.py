from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello! This is my first app on Azure App Service 🚀--Updated Version"

if __name__ == "__main__":
    app.run()