import requests

sign=input("Enter your Zodiac Sign:")

day=input("Please enter the sign(Today,Tomorrow or Yesterday):")


params = (
('sign', sign),
('day', day),
)

response =requests.get('https://aztro.sameerkumar.website/', params=params)


json=response.json()


print("Horoscope for",json.get('current_date'))
print(json.get('description'))
print("Compatability:",json.get('compatabality'))
print("Mood:",json.get('Mood'))
print("Color:",json.get('Color'))
print("Lucky Number:",json.get('lucky_number'))
print("Lucky Time:",json.get('lucky_time'))