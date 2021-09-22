from app.models.events import Meta


def get_events(regions: str) -> dict:
    regions_list = list(regions.split(","))
    events_model = Meta()
    return events_model.to_dict(regions_list)
