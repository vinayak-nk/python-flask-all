from urllib import response
import requests

BASE_URL = 'http://127.0.0.1:5000/'

data = [
  {'name':'test1', 'views': 10, 'likes': 11},
  {'name':'test2', 'views': 100, 'likes': 111},
  {'name':'test3', 'views': 1000, 'likes': 1111}
]
# response = requests.post(BASE_URL + 'video/3', {'name':'test', 'views': 10, 'likes': 11})
# print(response.json())

# input()

# response = requests.get(BASE_URL + 'video/11')
# print(response.json())

for i in range(len(data)):
  response = requests.post(BASE_URL + 'video/' + str(i), data[i] )
  print(response.json())
  
input()
reponse = requests.delete(BASE_URL + 'video/0')
print('delete repsonse', reponse)
input()

response = requests.get(BASE_URL + 'video/2')
print(response.json())
response = requests.get(BASE_URL + 'video/0')
print(response.json())
