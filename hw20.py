import requests

url = 'https://upload.wikimedia.org/wikipedia/commons/1/19/Europ%C3%A4ischer_Ziesel_in_Hockstellung.jpg'

response = requests.get(url)
#response.raise_for_status()

with open("image.jpg", "wb") as picture_file:
    picture_file.write(response.content)

print(response.content)






