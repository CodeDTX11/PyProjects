import requests
from datetime import datetime

### Practiced with HTTP post, put and delete requests with the pixela website api

# https://pixe.la/@dtxpixela

pixela_endpoint = "https://pixe.la/v1/users"

USERNAME = "dtxpixela"
TOKEN = "asdfoei3j34j3l24jklkj24jj9"
GRAPH_ID = "graph1"

create_user_params = {
    "token" : TOKEN,
    "username" : USERNAME,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes"
}

# 1 create a user
# response = requests.post(url=pixela_endpoint, json=create_user_params)
# print(response.text)

# 2 create a graph
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id" : GRAPH_ID,
    "name": "Coding Graph",
    "unit": "commit",
    "type": "int",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)

# print(response.text)

# 3 post a pixel

today = datetime.now()
# print(today.strftime("%Y%m%d"))
value = input("How many coding commits have you made today? ")
post_value_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": value
}
post_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

# post_response = requests.post(url=post_pixel_endpoint, json=post_value_params, headers=headers)
# print(post_response.text)

# 4 update pixel
# /v1/users/<username>/graphs/<graphID>/<yyyyMMdd>

pixel_date_to_update = datetime(year=2025, month=2, day=10)
print(pixel_date_to_update.strftime("%Y%m%d"))

update_params = {
    "quantity" : "100"
}

# update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{pixel_date_to_update.strftime("%Y%m%d")}"
#
# res = requests.put(url=update_pixel_endpoint, json=update_params, headers=headers)
#
# print(res.text)

# delete_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{pixel_date_to_update.strftime("%Y%m%d")}"
#
# requests.delete(url=delete_pixel_endpoint, headers=headers)