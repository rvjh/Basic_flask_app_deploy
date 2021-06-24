from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hi this is my first flask application. </h1>"


if __name__ == "__main__":
    app.run()
