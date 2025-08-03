from .functions import get_rare_items, get_quest_locations

# called after the game.json file has been loaded
def after_load_game_file(game_table: dict) -> dict:
    return game_table
# called after the items.json file has been loaded, before any item loading or processing has occurred
# if you need access to the items after processing to add ids, etc., you should use the hooks in World.py
def after_load_item_file(item_table: list) -> list:
    for item in get_rare_items():
        item_table.append({
            "name": item['ItemName'],
            "category": [item['ItemCategory']],
            "progression": False,
            "useful": True,
        })
    return item_table

# NOTE: Progressive items are not currently supported in Manual. Once they are,
#       this hook will provide the ability to meaningfully change those.
def after_load_progressive_item_file(progressive_item_table: list) -> list:
    return progressive_item_table

# called after the locations.json file has been loaded, before any location loading or processing has occurred
# if you need access to the locations after processing to add ids, etc., you should use the hooks in World.py
def after_load_location_file(location_table: list) -> list:
    for location in get_quest_locations(True):
        location_table.append({
            "name": location['Location'],
            "region": location['Region'],
#            "category": ["!Progression", location['Region']] if not (location['ProgAllowed'] == "TRUE") else [location['Region']],
# TODO: Figure out how to mark locations as not progression-safe
            "category": [location['Region']],
        })
    for i in range(1, 100):
        location_table.append({
            "name": f"Act 2 Dummy Location {i}",
            "region": "Act Two",
            "category": ["Dummy locations to be filled in later"]
        })
    for i in range(1, 100):
        location_table.append({
            "name": f"Act 3 Dummy Location {i}",
            "region": "Act Three: Rivington",
            "category": ["Dummy locations to be filled in later"]
        })
    return location_table

# called after the locations.json file has been loaded, before any location loading or processing has occurred
# if you need access to the locations after processing to add ids, etc., you should use the hooks in World.py
def after_load_region_file(region_table: dict) -> dict:
    return region_table

# called after the categories.json file has been loaded
def after_load_category_file(category_table: dict) -> dict:
    return category_table

# called after the meta.json file has been loaded and just before the properties of the apworld are defined. You can use this hook to change what is displayed on the webhost
# for more info check https://github.com/ArchipelagoMW/Archipelago/blob/main/docs/world%20api.md#webworld-class
def after_load_meta_file(meta_table: dict) -> dict:
    return meta_table

# called when an external tool (eg Univeral Tracker) ask for slot data to be read
# use this if you want to restore more data
# return True if you want to trigger a regeneration if you changed anything
def hook_interpret_slot_data(world, player: int, slot_data: dict[str, any]) -> bool:
    return False
