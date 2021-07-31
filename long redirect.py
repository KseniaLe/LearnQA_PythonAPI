import requests

url = 'https://playground.learnqa.ru/api/long_redirect'
response = requests.get(url)
print(response.status_code)
print(response.history)

first_response = response.history[0]
second_response = response.history[1]
third_response = response.history[2]
final_response  = response

print(first_response.url)
print(second_response.url)
print(third_response.url)
print(final_response.url)


