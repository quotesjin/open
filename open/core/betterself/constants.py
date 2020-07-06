from open.utilities.fields import create_django_choice_tuple_from_list


class BetterSelfResourceConstants:
    """
    RESTful constants used in URLs, useful for URL lookups
    """

    MEASUREMENTS = "measurements"
    INGREDIENTS = "ingredients"
    INGREDIENT_COMPOSITIONS = "ingredient_compositions"
    SUPPLEMENTS = "supplements"
    # note - changed the plural of this, before it was called supplements_stacks and that felt stupid
    SUPPLEMENT_STACKS = "supplement_stacks"
    SUPPLEMENT_STACK_COMPOSITIONS = "supplement_stack_compositions"
    SUPPLEMENT_LOGS = "supplement_logs"
    DAILY_PRODUCTIVITY_LOGS = "productivity_logs"
    SLEEP_LOGS = "sleep_logs"
    ACTIVITIES = "activities"
    ACTIVITY_LOGS = "activity_logs"
    WELL_BEING_LOG = "well_being_logs"


WEB_INPUT_SOURCE = "web"
TEXT_MSG_SOURCE = "text_message"
API_INPUT_SOURCE = "api"

BETTERSELF_LOG_INPUT_SOURCES = [
    API_INPUT_SOURCE,
    "ios",
    "android",
    "mobile",
    WEB_INPUT_SOURCE,
    "user_excel",
    TEXT_MSG_SOURCE,
]

INPUT_SOURCES_TUPLES = create_django_choice_tuple_from_list(
    BETTERSELF_LOG_INPUT_SOURCES
)


class BetterSelfFactoryConstants:
    # useful for generating fixtures
    DEFAULT_INGREDIENT_NAME_1 = "Leucine"
    DEFAULT_INGREDIENT_HL_MINUTE_1 = 50
    DEFAULT_INGREDIENT_DETAILS_1 = {
        "name": DEFAULT_INGREDIENT_NAME_1,
        "half_life_minutes": DEFAULT_INGREDIENT_HL_MINUTE_1,
    }

    DEFAULT_INGREDIENT_NAME_2 = "Valine"
    DEFAULT_INGREDIENT_HL_MINUTE_2 = 50
    DEFAULT_INGREDIENT_DETAILS_2 = {
        "name": DEFAULT_INGREDIENT_NAME_2,
        "half_life_minutes": DEFAULT_INGREDIENT_HL_MINUTE_2,
    }

    DEFAULT_INGREDIENT_NAME_3 = "Isoleucine"
    DEFAULT_INGREDIENT_HL_MINUTE_3 = 50
    DEFAULT_INGREDIENT_DETAILS_3 = {
        "name": DEFAULT_INGREDIENT_NAME_3,
        "half_life_minutes": DEFAULT_INGREDIENT_HL_MINUTE_3,
    }

    DEFAULT_MEASUREMENT_NAME = "milligram"
    DEFAULT_MEASUREMENT_SHORT_NAME = "mg"
    DEFAULT_MEASUREMENT_DETAILS = {
        "name": DEFAULT_INGREDIENT_NAME_1,
        "short_name": DEFAULT_MEASUREMENT_SHORT_NAME,
    }
