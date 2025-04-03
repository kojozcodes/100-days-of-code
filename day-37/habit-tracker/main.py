from datetime import datetime
import requests

USERNAME = "kojozcodes"
TOKEN = None
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_parameters)
# print(response.text)
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "My Coding Graph",
    "unit": "hour",
    "type": "int",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

today = datetime.now()
yesterday = datetime(year=2025, month=4, day=2)

pixel_config = {
    "date": yesterday.strftime("%Y%m%d"),
    "quantity": "2",
}

# response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
# print(response.text)

update_endpoint = f"{pixel_endpoint}/{yesterday.strftime("%Y%m%d")}"

yesterday_data = {
    "quantity": "3",
}

# response = requests.put(url=update_endpoint, json=yesterday_data, headers=headers)
# print(response.text)

delete_endpoint = update_endpoint

response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)

# //////h/f#i@e!d!ei!k3!4!n4i2!2!nl!k///////
