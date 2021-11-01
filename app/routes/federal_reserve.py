from typing import Union

from flask import Blueprint, jsonify

from app.repositories.federal_reserve.fomc_statements import \
    FOMC_Statement_Repo

blueprint = Blueprint("federal_reserve", __name__)


@blueprint.route("/fed/get-fomc-statement/", defaults={'dates': None})
@blueprint.route("/fed/get-fomc-statement/<dates>")
def get_fomc_statements(dates: Union[str, None]):
    return jsonify(FOMC_Statement_Repo(dates).get_data())
