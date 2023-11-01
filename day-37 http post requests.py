import requests
from datetime import datetime

# ----------------------------------------------------------------------------
# -1
USERNAME = "vhsol"
TOKEN = "sfdfvvnndfvjnfhj"
GRAPH_ID = "graph1"
DATE = "today.strftime('%Y%m%d')"
# ----------------------------------------------------------------------------

pixela_endpoint = " https://pixe.la/v1/users"

# ----------------------------------------------------------------------------
user_parms = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# ----------------------------------------------------------------------------
# response = requests.post(url=pixela_endpoint, json=user_parms)
# print(response.text)
# ----------------------------------------------------------------------------

# -2
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
# ----------------------------------------------------------------------------
graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling_Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",
}
# ----------------------------------------------------------------------------
headers = {
    'X-USER-TOKEN': TOKEN,
}
# ----------------------------------------------------------------------------
# response = requests.post(
#      url=graph_endpoint, json=graph_config, headers=headers)

# print(response.text)
# ----------------------------------------------------------------------------


# -3
Creation_piexel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime(year=2023, month=7, day=2)
# print(today)
# ----------------------------------------------------------------------------
pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "7.56",

}
# ----------------------------------------------------------------------------
# response = requests.post(url=Creation_piexel_endpoint,
#                          json=pixel_data, headers=headers)
# print(response.text)

# ------------------------------------------------------------------------------

# -4
add_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

PUT_pixel_data = {
    "quantity": "8.94",

}

# response = requests.put(url=add_pixel_endpoint,
#                         json=PUT_pixel_data, headers=headers)
# print(response.text)
# --------------------------------------------------------------------------------------

# -5
delete_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

response = requests.delete(url=delete_pixel_endpoint, headers=headers)
print(response.text)
