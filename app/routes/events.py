from flask import Blueprint, jsonify, request

from app.repositories import events as events_repo

blueprint = Blueprint("events", __name__)


@blueprint.route("/events/get-econ-events", methods=["POST"])
def get_econ_events():
    req_data = (request.data).decode("utf-8")
    req_data = list(req_data.split(","))
    output = events_repo.get_events(req_data)

    return jsonify(output), 200
