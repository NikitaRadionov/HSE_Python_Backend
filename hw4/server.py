from flask import Flask, request, jsonify
from controllers import operation
from dotenv import dotenv_values

app = Flask(__name__)


def get_port() -> int:
    config = dotenv_values(".env")
    if "PORT" in config:
        return config["PORT"]
    return 5000

def get_debug() -> bool:
    config = dotenv_values(".env")
    if "DEBUG" in config:
        return config["DEBUG"]
    return True


@app.route("/")
def server_info():
    return "My server"

@app.route("/author")
def author():
    author = {
        "name": "Nikita",
        "course": 2,
        "age": 22,
    }
    return jsonify(author)

@app.route("/sum")
def runner():
    a = request.args.get('a', type=int)
    b = request.args.get('b', type=int)
    return jsonify({'sum': operation(a, b)})


if __name__ == "__main__":
    app.run(debug=get_debug(), port=get_port())