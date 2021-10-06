'''request.py receives JSON inputs, uses the trained model to make a prediction and returns that prediction 
in JSON format which can be accessed through the API endpoint.'''

import requests

url = 'http://localhost:5000/results'
r = requests.post(url,json={'variance':2, 'skewness':3, 'curtosis':4, 'entropy':1})

print(r.json())