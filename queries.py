import requests

url = "https://playground.learnqa.ru/ajax/api/compare_query_type"

def print_status(response) :
    print(response.status_code)
    print(response.text)

print()
print('Reqsuests without method')
print()

response = requests.get(url)
print_status(response)
response = requests.put(url)
print_status(response)
response = requests.post(url)
print_status(response)
response = requests.delete(url)
print_status(response)

print()
print('Head request')
print()

response = requests.head(url)
print_status(response)

print()
print('Reqsuests with method')
print()

response = requests.get(url, params={'method': 'GET'})
print_status(response)
response = requests.put(url, data={'method': 'PUT'})
print_status(response)
response = requests.post(url, data={'method': 'POST'})
print_status(response)
response = requests.delete(url, data={'method': 'DELETE'})
print_status(response)


print()
print('Cycle request')
print()

method = ['GET', 'PUT', 'POST', 'DELETE']

for method_type in method :
    print(method_type)
    response = requests.get(url, params = {"method": method_type})
    print_status(response)


print()
print()

method = ['GET', 'PUT', 'POST', 'DELETE']
for method_type in method :
    print(method_type)
    response = requests.put(url, data={"method": method_type})
    print_status(response)

print()
print()

method = ['GET', 'PUT', 'POST', 'DELETE']
for method_type in method:
    print(method_type)
    response = requests.post(url, data={"method": method_type})
    print_status(response)

print()
print()

method = ['GET', 'PUT', 'POST', 'DELETE']
for method_type in method:
    print(method_type)
    response = requests.delete(url, data={"method": method_type})
    print_status(response)


