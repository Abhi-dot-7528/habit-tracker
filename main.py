import requests

USERNAME = "enzo"
TOKEN = "us8heq#9wjd30_3h2!H*"

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
    "id": "graph0",
    "name": "Go To Sleep Graph",
    "unit": "Hours",
    "type": "float",
    "color": "ichou"
}
header = {
    "X-USER-TOKEN": TOKEN
}
graph_post = f"{pixela_url}/{USERNAME}/graphs"
response = requests.post(url=graph_post, json=graph_config, headers=header)
print(response.text)
