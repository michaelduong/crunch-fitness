import requests
import json

tustin_url = "https://www.crunch.com/crunch_core/clubs/143"
fountain_valley_url = "https://www.crunch.com/crunch_core/clubs/52"

current_tustin_capacity = 0
max_tustin_capacity = 0
current_fv_capacity = 0
max_fv_capacity = 0

tustin_res = requests.get(tustin_url)
fountain_valley_res = requests.get(fountain_valley_url)

if tustin_res.status_code == 200:
    json_response_tustin = tustin_res.json()
    max_tustin_capacity = json_response_tustin["max_occupancy"]
    current_tustin_capacity = json_response_tustin["current_occupancy"]
    percent_full_tustin = str(round((current_tustin_capacity / max_tustin_capacity) * 100, 2))

if fountain_valley_res.status_code == 200:
    json_response_fv = fountain_valley_res.json()
    max_fv_capacity = json_response_fv["max_occupancy"]
    current_fv_capacity = json_response_fv["current_occupancy"]
    percent_full_fv = str(round((current_fv_capacity / max_fv_capacity) * 100, 2))

print("Tustin Crunch gym is currently " + str(current_tustin_capacity) + "/" + str(max_tustin_capacity) + " " + "(" + percent_full_tustin + "% full)")
print("Fountain Valley Crunch gym is currently " + str(current_fv_capacity) + "/" + str(max_fv_capacity) + " " + "(" + percent_full_fv + "% full)")
