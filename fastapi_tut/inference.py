import requests


BASE_URL = "http://127.0.0.1:8000"

response = requests.get(f"{BASE_URL}/xyz_name")
print(response.text)

payload = {
    "name": "TYR",
    "roll no.": "B26CI45",
    "gender": "male",
    "subjects enrolled": "AI, CV, NLU, DL, ML",
    "CGPA": 7.9
}
response = requests.post(f"{BASE_URL}/create_student", json=payload)
print(response.text)

response = requests.get(f"{BASE_URL}/status", params={"roll_number": "B26CI45"})
print(response.json())

response = requests.put(f"{BASE_URL}/modify_student", params={"roll_number": "B26CI45"})
# response = requests.put(f"{BASE_URL}/modify_student?roll_number=B26CI45) also works the same
# Same is for the delete request also
print(response.text)

response = requests.delete(f"{BASE_URL}/delete_student", params={"roll_number": "B26CI45"})
print(response.text)
