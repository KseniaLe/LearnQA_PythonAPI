import requests, time

url = "https://playground.learnqa.ru/ajax/api/longtime_job"
'''
создаём задачу
'''
response1 = requests.get(url)
print(response1)
print(response1.text)
'''
парсим json из ответа
'''
parsed_response1_json_text = response1.json()
print(parsed_response1_json_text["token"])
print(parsed_response1_json_text["seconds"])
request_token = {"token": parsed_response1_json_text["token"]}
request_seconds = {"seconds": parsed_response1_json_text["seconds"]}
print(request_token)
print(request_seconds)
'''
делаем запрос с token, смотрим статус
'''
response2 = requests.get(url, params = request_token )
print(response2)
print(response2.text)
'''
ждём нужно кол-во секунд, смотрим статус
'''
t = parsed_response1_json_text["seconds"]
time.sleep(t)
response3 = requests.get(url, params = parsed_response1_json_text)
print(response3)
print(response3.text)