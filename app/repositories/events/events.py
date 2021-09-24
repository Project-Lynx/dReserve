from app.models.events import Meta


# Get events of specific region(s) from db
def get_events(regions: str) -> dict:
    regions_list = list(regions.split(","))
    events_model = Meta()
    return events_model.to_dict(regions_list)


# Handle logic behind regions input
def handle_events(regions: str) -> dict:
    if "," in regions:
        return get_events(regions)
    else:
        regions = regions + ","
        return get_events(regions)
