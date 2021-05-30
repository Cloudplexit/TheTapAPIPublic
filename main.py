# main.py
import os

from flask import Flask, jsonify, request

from best_time_client import BestTimeClient
from client import Client
from errors import PrimaryServerException
from filter import filter_by_date_range, validate, filter_by_id, filter_by_venue_name

app = Flask(__name__)


@app.route("/items-by-category")
# health check function that returns "Hello world!"
def index():
    return "Hello world!"


@app.route("/items-by-category/from-date-range", methods=["GET"])
def get_items_by_category_from_date_range():
    start = request.args.get('start')  # dd-mm-yyyy
    end = request.args.get('end')

    if not validate(start):
        return jsonify({"message": "Incorrect data format for start, should be YYYY-MM-DD"}), 400
    if not validate(end):
        return jsonify({"message": "Incorrect data format for end, should be YYYY-MM-DD"}), 400

    client = Client(app.config.get("RESULT_NO_1"))
    try:
        data = client.get()
        return jsonify({"items": filter_by_date_range(data, start, end)}), 200
    except PrimaryServerException as e:
        return jsonify({"error": e.message}), 500


@app.route("/items-by-category/from-id", methods=["GET"])
def get_items_by_category_from_id():
    event_id = request.args.get('id')
    client = Client(app.config.get("RESULT_NO_1"))

    try:
        data = client.get()
        return jsonify(filter_by_id(data, int(event_id))), 200
    except PrimaryServerException as e:
        return jsonify({"error": e.message}), 500


@app.route("/items-by-category/best-time", methods=["GET"])
def get_items_by_category_best_time():
    venue_name = request.args.get('venue_name')
    client = Client(app.config.get("RESULT_NO_2"))

    try:
        data = client.get()
        location = filter_by_venue_name(data, venue_name)
        best_time_client = BestTimeClient(app.config.get("BEST_TIME_API_KEY_PRIVATE"))
        best_time = best_time_client.get(location['title'], location['address'])
        location['best_time'] = best_time
        return jsonify(location)
    except PrimaryServerException as e:
        return jsonify({"error": e.message}), 500


# Checks to see if the name of the package is the run as the main package.
if __name__ == "__main__":
    # load configs
    app.config.from_pyfile(os.path.join(".", "config/app.conf"), silent=False)
    # Runs the Flask application only if the main.py file is being run.
    # app.run()
    app.run(host='127.0.0.1', port=app.config.get("APP_PORT"))
