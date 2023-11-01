# nesting
capiatals = {"france": "paris",
             "germeny": "berlin"
             }
# -------------------------------------------------------------------------

# nested list in dictionary
# you can add multiple value in one key

travel_log = {
    "France": ["paris", "lile", "djanho"],
    "Germeny": ["Berlin", "handburg", "strupat"],
}
# ---------------------------------------------------------------------------

# nesting dictionary in a dictionary
travel_log = {
    "France": {"city_visted": ["paris", "lile", "djanho"], "total_visits": 12},

    "Germeny": {"city_followup": ["Berlin", "handburg", "strupat"], "money-required": "234$"},
}

print(travel_log["Germeny"])

#----------------------------------------------------------------------------

# Nesting Dictionary in list

travel_log = [
    {"country":"France",
      "city_visted": ["paris", "lile", "djanho"],
      "total_visits": 12},
      

    {"country":"Germeny",
      "city_followup": ["Berlin", "handburg", "strupat"], 
      "money-required": "234$"},
]
