import requests
import json

url = "https://flask-app-demo.onrender.com/predict?level=Junior&lang=Java&tweets=yes&phd=no"

response = requests.get(url = url)

# first thing, check the response's status_code


print(response.status_code)
if response.status_code == 200:
    print(response.json())
    json_object = json.loads(response.text)
    print(json_object)
    pred = json_object["prediction"]
    print("prediction: ", pred)