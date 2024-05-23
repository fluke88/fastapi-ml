import requests
import json

# Отправка запроса на предсказание стоимости
url = 'http://localhost:8080/predict'
data = [['2021-03-19', 56.9989, 70.48573, 2, 1, 1, 1, 20, 10, 1, 2, 'Санкт-Петербург']]
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
response = requests.get(url, data=json.dumps(data), headers=headers)

# Печать ответа
print(response.status_code)
print(response.json())
