from flask import Blueprint, jsonify

from app.repositories.yields import curve, rate

blueprint = Blueprint("yields", __name__)


@blueprint.route("/yields/get-curve/<product>/<dates>")
def get_curve(product, dates):
    req_data = [product, dates]
    return jsonify(curve.handler(req_data)), 200


@blueprint.route("/yields/get-rate/<product>/<duration>/", defaults={'dates': None})
@blueprint.route("/yields/get-rate/<product>/<duration>/<dates>")
def get_rate(product, duration, dates):
    req_data = [product, duration, dates]
    return jsonify(rate.handler(req_data)), 200
