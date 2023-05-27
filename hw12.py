import requests
url = 'https://dummyjson.com/users?limit=100'
response = requests.get(url)
data = response.json()

louisville_citizen = [user for user in data["users"] if user["address"].get("citi", '') == "louisville"]
man_with_brown_hair = [user["age"] for user in data["users"] if user["gender"] == "male" and user["hair"]["color"] == 'Brown']
if man_with_brown_hair:
    average_age_man_with_brown_hair = sum(man_with_brown_hair) / len(man_with_brown_hair)
    print("середній вік чоловіків з Brown волоссям:", average_age_man_with_brown_hair)
print("список людей, що проживають в місті Louisville:")
for person in louisville_citizen:
    print(person['firstName'], person['lastName'])

