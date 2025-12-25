import requests

BASE_URL = "http://127.0.0.1:5000"

home_response = requests.get(f"{BASE_URL}")
print(home_response.text)

payload = {
    "name": "XYZ",
    "rollno": "ABC"
}

json_response = requests.post(f"{BASE_URL}/profile_json", json=payload)
print(json_response.json())
