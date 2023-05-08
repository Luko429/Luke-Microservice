# Investment Growth Rate Microservice for Luke's project 

This microservice calculates the investment growth rate using the formula:
Growth Rate = ((newest_value/oldest_value)^(1/(total years - 1)) - 1)*100


## How to request data from the microservice

To request data from the microservice, send a POST request with a JSON object containing the data in the following format:

```json
{
  "data": [newest_value, oldest_value, total_years]
}

For example: 

import requests
import json

data = {
    "data": [300, 500, 11]
}

response = requests.post('http://127.0.0.1:5000/calculate_growth_rate', json=data)


## How to receive data from the microservice

The microservice will return a JSON object containing the calculated growth rate as the answer key. To receive the data, you can use the json() method of the requests library's response object:

result = response.json()
print(result)

The output should look like this:

{
  "answer": 5
}


## UML Diagram: 

![Untitled 24.png](Untitled%2024.png)
