import requests

#petition = requests.get("http://protecounam.mx/home", timeout=1)

# Status code
#print(petition.status_code)

# No format
#print(petition.content)

# Format
#print(petition.text)

req_json = requests.get("https://api.github.com/users/EdgarRamirezFuentes", timeout=1)

#print(req_json.json())

# HEADERS
#print(req_json.headers)

# POST petitions
data = {
    "user" : "edgar",
    "password" : "123"
}

req_post = requests.post("https://httpbin.org/post", data=data)

#print(req_post.text)
#print(req_post.json())

# Getting an image using requests
req_img = requests.get('http://protecounam.mx/img/base/principal_1.png')

with open('./image.png', 'wb') as file:
    file.write(req_img.content)

