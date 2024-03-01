import requests

response = requests.get('http://127.0.0.1:8000/api/groups/manager/users/')

if response.status_code == 200:
    print(response.json())  # Assuming your endpoint returns JSON data
else:
    print(f"Error: {response.status_code}")

