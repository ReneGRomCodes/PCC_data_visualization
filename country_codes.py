from pygal_maps_world.i18n import COUNTRIES

# Mapping of special cases where country names differ from those in Pygal
SPECIAL_CASES = {
    "Bolivia": "bo",
    "Congo, Dem. Rep.": "cd",
    "Congo, Rep.": "cg",
    "Egypt, Arab Rep.": "eg",
    "Gambia, The": "gn",
    "Iran, Islamic Rep.": "ir",
    "Korea, Dem. Rep.": "kp",
    "Korea, Rep.": "kr",
    "Kyrgyz Republic": "kg",
    "Libya": "ly",
    "Macedonia, FYR": "mk",
    "Moldova": "md",
    "Slovak Republic": "sk",
    "Tanzania": "tz",
    "Venezuela, RB": "ve",
    "Vietnam": "vn",
    "Yemen, Rep.": "ye",
    "Lao PDR": "la"
}


def get_country_code(country_name):
    """Return the Pygal 2-digit country code for the given country."""

    # Check if country name has a special case mapping
    if country_name in SPECIAL_CASES:
        return SPECIAL_CASES[country_name]

    # Check for country name in Pygal countries dictionary
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code

    return None
