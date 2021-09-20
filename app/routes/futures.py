from flask import Blueprint, jsonify, request

from app.repositories import futures as futures_repo

blueprint = Blueprint("futures", __name__)


@blueprint.route("/futures/get-hist", methods=["POST"])
def get_hist():
    req_data = (request.data).decode("utf-8")
    hist_data = futures_repo.get_hist(req_data)

    return jsonify(hist_data), 200


@blueprint.route("/futures/get-quotes", methods=["POST"])
def get_quotes():
    req_data = (request.data).decode("utf-8")
    symbols = list(req_data.split(","))
    quotes_data = futures_repo.get_quotes(symbols)

    return jsonify(quotes_data), 200
