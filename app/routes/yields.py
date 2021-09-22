from flask import Blueprint, jsonify, request

from app.repositories import yields as yields_repo

blueprint = Blueprint("yields", __name__)


@blueprint.route("/yields/get-curve", methods=["POST"])
def get_curve():
    req_data = (request.data).decode("utf-8")
    return jsonify(yields_repo.handle_get_curve(req_data)), 200


@blueprint.route("/yields/get-rate", methods=["POST"])
def get_rate():
    req_data = (request.data).decode("UTF-8")
    return jsonify(yields_repo.handle_get_rate(req_data)), 200
