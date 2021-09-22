from flask import Blueprint, jsonify, request

from app.repositories import futures as futures_repo

blueprint = Blueprint("futures", __name__)


@blueprint.route("/futures/get-hist", methods=["POST"])
def get_hist():
    req_data = (request.data).decode("utf-8")
    return jsonify(futures_repo.get_hist(req_data)), 200


@blueprint.route("/futures/get-quotes", methods=["POST"])
def get_quotes():
    req_data = (request.data).decode("utf-8")
    return jsonify(futures_repo.get_quotes(req_data)), 200
