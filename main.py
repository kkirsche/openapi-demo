#!/usr/bin/env python3

from flask import Flask, jsonify, abort, make_response, request

# fighters - This is a list of fighters holding UFC championships.
# This data is representative of what we might retrieve from a SQL
# database or other data source to provide via an API.
fighters = [
    {
        "id": 1,
        "name": "Daniel Cormier",
        "weightclass": "Heavyweight (Up to 265 pounds)",
    },
    {"id": 2, "name": "Jon Jones", "weightclass": "Light heavyweight (205 lbs)"},
    {"id": 3, "name": "Robert Whittaker", "weightclass": "Middleweight (185 lbs)"},
    {"id": 4, "name": "Kamaru Usman", "weightclass": "Welterweight (170 lbs)"},
    {"id": 5, "name": "Khabib Nurmagomedov", "weightclass": "Lightweight (155 lbs)"},
    {"id": 6, "name": "Max Holloway", "weightclass": "Men's featherweight (145 lbs)"},
    {"id": 7, "name": "Henry Cejudo", "weightclass": "Men's bantamweight (135 lbs)"},
    {"id": 8, "name": "Henry Cejudo", "weightclass": "Men's flyweight (125 lbs)"},
    {"id": 9, "name": "Amanda Nunes", "weightclass": "Women's featherweight (145 lbs)"},
    {"id": 10, "name": "Amanda Nunes", "weightclass": "Women's Bantamweight (135 lbs)"},
    {
        "id": 11,
        "name": "Valentina Shevchenko",
        "weightclass": "Women's flyweight (125 lbs)",
    },
    {"id": 12, "name": "Jessica Andrade", "weightclass": "Strawweight (115 lbs)"},
]

# app is the WSGI application which runs the web server.
app = Flask(__name__)


# !-- Begin application routes --!
@app.route("/api/v1/fighters", methods=["GET"])
def index():
    return jsonify(fighters)


@app.route("/api/v1/fighters/<int:fighter_id>", methods=["GET"])
def show(fighter_id):
    fighter = [fighter for fighter in fighters if fighter["id"] == fighter_id]
    if len(fighter) == 0:
        abort(404)
    return jsonify({"fighter": fighter[0]})


@app.route("/api/v1/fighters", methods=["POST"])
def create():
    if (
        not request.json
        or "name" not in request.json
        or "weightclass" not in request.json
    ):
        abort(400)
    fighter = {
        "id": fighters[-1]["id"] + 1,
        "name": request.json["name"],
        "weightclass": request.json["weightclass"],
    }

    fighters.append(fighter)
    return jsonify({"fighter": fighter}), 201


@app.route("/api/v1/fighters/<int:fighter_id>", methods=["PUT"])
def update(fighter_id):
    fighter = [fighter for fighter in fighters if fighter["id"] == fighter_id]
    if len(fighter) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if "name" not in request.json and type(request.json.get("name")) != str:
        abort(400)
    if "weightclass" not in request.json and type(request.json.get("weightclass")) != str:
        abort(400)

    fighter[0]["name"] = request.json.get("name", fighter[0]["name"])
    fighter[0]["weightclass"] = request.json.get(
        "weightclass", fighter[0]["weightclass"]
    )

    return jsonify({"fighter": fighter[0]})


@app.route("/api/v1/fighters/<int:fighter_id>", methods=["DELETE"])
def destroy(fighter_id):
    fighter = [fighter for fighter in fighters if fighter["id"] == fighter_id]
    if len(fighter) == 0:
        abort(404)
    fighters.remove(fighter[0])
    return jsonify({"fighter": fighter[0]})


@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({"error": "400 - Bad Request"}), 400)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({"error": "404 - Not Found"}), 404)


if __name__ == "__main__":
    app.run(debug=True)
