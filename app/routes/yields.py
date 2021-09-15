from typing import Union

from flask import Blueprint, request

from app.repositories import yields as yields_repo

blueprint = Blueprint("yields", __name__)


@blueprint.route("/get-curve", methods=["POST"])
def get_curve() -> Union[str, dict]:
    req_data = (request.data).decode("utf-8")

    if "," in req_data:
        data_list = list(req_data.split(","))
        product = data_list[0]
        if data_list[1] == "MOST_RECENT":
            return yields_repo.get_curve(product, mr=True)
        else:
            dates = data_list[1:]
            if len(dates) <= 1:
                return yields_repo.get_curve(product, dates=str(data_list[1]))
            else:
                return yields_repo.get_curve(product, dates=dates)

    elif isinstance(req_data, str):
        if req_data == "":
            return   """Empty POST request, send data as the following:
                        Product,Date1(YYYY-MM-DD),...,Datex(YYYY-MM-DD)
                     """
        else:
            return yields_repo.get_curve(req_data)


@blueprint.route("/get-rate", methods=["POST"])
def get_rate() -> dict:
    req_data = (request.data).decode("UTF-8")

    if "," in req_data:
        data_list = list(req_data.split(","))
        product = data_list[0]
        duration = data_list[1]

        if len(req_data) == 2:
            output = yields_repo.get_rate(product, duration)

        else:
            dates = req_data[2:]
            output = yields_repo.get_rate(product, duration, dates)

            if len(dates) <= 1:
                date = str(req_data[2])
                output = yields_repo.get_rate(product, duration, date)

    return output
