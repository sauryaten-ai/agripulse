CROP_RULES = {

    "TOMATO": {
        "ph_range": (6.0, 7.0),
        "key_nutrient": "K",
        "high_demand_threshold": 200
    },

    "WHEAT": {
        "ph_range": (6.0, 7.5),
        "key_nutrient": "N",
        "high_demand_threshold": 30
    },

    "RICE": {
        "ph_range": (5.0, 6.5),
        "key_nutrient": "P",
        "high_demand_threshold": 25
    },

    "MAIZE": {
        "ph_range": (5.8, 7.0),
        "key_nutrient": "N",
        "high_demand_threshold": 35
    }

}

UNIVERSAL_THRESHOLDS = {
    "N": 20,
    "P": 15,
    "K": 150
}