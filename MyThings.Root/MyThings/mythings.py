
from app import create_app

from flask import Flask

# app = create_app()

app = Flask(__name__)

@app.route("/hello")
def hello():
    return "hello"


from flask import Blueprint
test_blue = Blueprint("test", __name__)

app.register_blueprint(test_blue)

@test_blue.route("/")
def test():
    return "Hello"


if __name__ == "__main__":
    print(app.url_map)
    app.run()
