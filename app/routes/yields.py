from typing import Union

from flask import Blueprint, jsonify
from werkzeug.wrappers import Response

from app.repositories.yields.yields_repo import Yields_Repo

blueprint = Blueprint("yields", __name__)


@blueprint.route("/yields/get-curve/<product>/", defaults={'dates': None})
@blueprint.route("/yields/get-curve/<product>/<dates>")
def get_curve(product: str, dates: Union[str, None]) -> Response:
    """Get all available durations for a product (the yield curve)."""
    output = Yields_Repo(
        {"dates": dates, "product": product, "duration": None},
    ).get_data()
    return jsonify(output)


@blueprint.route("/yields/get-rate/<product>/<duration>/", defaults={'dates': None})
@blueprint.route("/yields/get-rate/<product>/<duration>/<dates>")
def get_rate(product: str, dates: Union[str, None], duration: str) -> Response:
    """Get specific rates for a product."""
    output = Yields_Repo(
        {"dates": dates, "product": product, "duration": duration},
    ).get_data()
    return jsonify(output)
