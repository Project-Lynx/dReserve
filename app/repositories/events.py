from app.models.events import Meta


def get_events(regions: list) -> dict:
    events_model = Meta()
    return events_model.to_dict(regions)
