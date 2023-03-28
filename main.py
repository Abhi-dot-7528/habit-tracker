import requests

pixela_url = "https://pixe.la/v1/users"
user_params = {
    "token": "us8heq#9wjd30_3h2!H*",
    "username": "enzo",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

post_response = requests.post(url=pixela_url, json=user_params)
print(post_response.text)
