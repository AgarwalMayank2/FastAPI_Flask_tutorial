from flask import Flask, jsonify, request
from markupsafe import escape

app = Flask(__name__)  # Initializing an instance of the Flask class


@app.route("/", methods=["GET", "POST"])  # Decorator for base url
def base_url():  # Action to be taken
    return "Hello world"


@app.route("/<name>", methods=["GET", "POST"])  # Variable defining
def profile(name):
    escaped_name = escape(name)
    return f"Profile of {escaped_name}"


@app.route("/profile_json", methods=["POST"])
# POST have a different format of request in which data is separate
# from the url so we can directly take that data
def profile_json():
    data = request.get_json()
    return jsonify({
        "name": escape(data["name"]),
        "rollno": escape(data["rollno"])
    })


app.run(debug=True)
# Running the app in debug mode means that the changes in code are reflected
# while the app is running
