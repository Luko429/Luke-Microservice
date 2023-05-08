import requests
import json

data = {
    "data": [700, 200, 5]
}

response = requests.post('http://127.0.0.1:5000/calculate_growth_rate', json=data)
result = json.loads(response.text)

print(result)
