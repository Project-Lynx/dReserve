from flask import Blueprint, jsonify

from app.repositories.events import events

blueprint = Blueprint("events", __name__)


# Route to get events for specific region(s) (if multiple regions use ",")
@blueprint.route("/events/get-econ-events/<regions>")
def get_econ_events(regions):
    return jsonify(events.handle_events(regions)), 200
