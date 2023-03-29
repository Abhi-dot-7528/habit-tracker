import requests
from datetime import datetime

USERNAME = "enzo"
TOKEN = "us8heq#9wjd30_3h2!H*"
GRAPH_ID = "graph0"

pixela_url = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# post_response = requests.post(url=pixela_url, json=user_params)
# print(post_response.text)

graph_config = {
    "id": GRAPH_ID,
    "name": "Go To Sleep Graph",
    "unit": "Hours",
    "type": "float",
    "color": "ichou"
}
header = {
    "X-USER-TOKEN": TOKEN
}
graph_post = f"{pixela_url}/{USERNAME}/graphs"
# response = requests.post(url=graph_post, json=graph_config, headers=header)
# print(response.text)

today = datetime.now()

pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "6.0"
}
pixel_post = f"{pixela_url}/{USERNAME}/graphs/{GRAPH_ID}"
response = requests.post(url=pixel_post, json=pixel_config, headers=header)
print(response.text)
