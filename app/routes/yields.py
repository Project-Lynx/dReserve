from flask import Blueprint, jsonify, request

from app.repositories import yields as yields_repo

blueprint = Blueprint("yields", __name__)

@blueprint.route("/get-curve", methods=["POST"])
def get_curve():
    req_data = (request.data).decode("utf-8")

    if "," in req_data:
        req_data = list(req_data.split(","))
        product = req_data[0]
        dates = req_data[1:]
        if len(dates) <= 1:
            dates = str(req_data[1])
        print(dates)
        output = yields_repo.get_curve(product, dates)

    elif isinstance(req_data, str):
        if req_data == "":
            output = """Empty POST request, send data as the following:
                        Product,Date1(YYYY-MM-DD),...,Datex(YYYY-MM-DD)
                     """
        else:
            output = yields_repo.get_curve(req_data)

    return output


@blueprint.route("/get-rate", methods=["POST"])
def get_rate():
    req_data = (request.data).decode("UTF-8")

    if "," in req_data:
        req_data = list(req_data.split(","))
        product = req_data[0]
        duration = req_data[1]

        if len(req_data) == 2:
            print("HIT!")
            output = yields_repo.get_rate(product, duration)

        else:
            dates = req_data[2:]
            output = yields_repo.get_rate(product, duration, dates)

            if len(dates) <= 1:
                date = str(req_data[2])
                output = yields_repo.get_rate(product, duration, date)

        return output
