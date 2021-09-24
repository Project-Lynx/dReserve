from flask import Blueprint, jsonify

from app.repositories.futures import hist, quote

blueprint = Blueprint("futures", __name__)


@blueprint.route("/futures/get-hist/<symbols>", methods=["GET"])
def get_hist(symbols):
    return jsonify(hist.handler(symbols)), 200


@blueprint.route("/futures/get-quote/<symbols>", methods=["GET"])
def get_quotes(symbols):
    return jsonify(quote.handler(symbols)), 200
