# Object classes from AP that represent different types of options that you can create
from Options import FreeText, NumericOption, Toggle, DefaultOnToggle, Choice, TextChoice, Range, NamedRange

# These helper methods allow you to determine if an option has been set, or what its value is, for any player in the multiworld
from ..Helpers import is_option_enabled, get_option_value



####################################################################
# NOTE: At the time that options are created, Manual has no concept of the multiworld or its own world.
#       Options are defined before the world is even created.
#
# Example of creating your own option:
#
#   class MakeThePlayerOP(Toggle):
#       """Should the player be overpowered? Probably not, but you can choose for this to do... something!"""
#       display_name = "Make me OP"
#
#   options["make_op"] = MakeThePlayerOP
#
#
# Then, to see if the option is set, you can call is_option_enabled or get_option_value.
#####################################################################


# To add an option, use the before_options_defined hook below and something like this:
#   options["total_characters_to_win_with"] = TotalCharactersToWinWith
#
class RandomizeGear(Toggle):
    """Items are items in the multiworld."""
    display_name = "Randomize Gear"
    default = True
    description = "If enabled, all equipment of Rare+ quality (and a few overpowered uncommons) will be items sent in the multiworld. Recommended."

class IncludeGearAsLocations(Toggle):
    """Items are locations."""
    display_name = "Randomize Gear"
    default = False
    description = "If enabled, all places you would normally get a Rare+ item instead sends a check. Not implemented."

class IncludeMissibleQuests(Toggle):
    """Missible quests are locations."""
    display_name = "Include Missible Quests"
    default = True
    description = "If enabled, missible quests will be locations. These will not have progression. Not recommended for release OFF worlds."

class IncludeAdditionalProgression(Toggle):
    """Additional progression items."""
    display_name = "Include Additional Progression Requirements"
    default = False
    description = "If enabled, additional progression will be required for major transitions, such as Underdark, Grymforge, Act 2, etc. Not currently recommended."

#class AdditionalProgressionLevels(NumericOption):
#    """Additional progression levels."""
#    display_name = "Additional Progression Levels"
#    default = 0
#    min_value = 0
#    max_value = 10
#    description = "If enabled, additional progression levels will be scattered through the world. Not recommended."

class IncludeFeatsAsItems(Toggle):
    """Feats are items."""
    display_name = "Include Feats as Items"
    default = False
    description = "If enabled, debug items that grant feats to the holder will be items in the multiworld, and the player can only select stat boosts on feat level-ups. Not implemented."

#class IncludeStatBoostsAsItems(NumericOption):
#    """Stat boosts are items."""
#    display_name = "Include Stat Boosts as Items"
#    default = 0
#    min_value = 0
#    max_value = 40
#    description = "This is how many '+2 to a random stat' debug items will be added to the world's items. Not implemented."

# This is called before any manual options are defined, in case you want to define your own with a clean slate or let Manual define over them
def before_options_defined(options: dict) -> dict:
    options["randomize_gear"] = RandomizeGear
    options["include_gear_as_locations"] = IncludeGearAsLocations
    options["include_missible_quests"] = IncludeMissibleQuests
    options["include_additional_progression"] = IncludeAdditionalProgression
#    options["additional_progression_levels"] = AdditionalProgressionLevels
    options["include_feats_as_items"] = IncludeFeatsAsItems
#    options["include_stat_boosts_as_items"] = IncludeStatBoostsAsItems
    return options

# This is called after any manual options are defined, in case you want to see what options are defined or want to modify the defined options
def after_options_defined(options: dict) -> dict:
    return options