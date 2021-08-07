import requests

url = "https://playground.learnqa.ru/api/homework_header"
response = requests.get(url)
print(response.status_code)
print(response.text)
print(response.headers)

class TestGetHeader:
    def test_get_header(self):
        url = "https://playground.learnqa.ru/api/homework_header"
        response = requests.get(url)
        headers_value = response.headers
        print(headers_value)

        assert headers_value !=None, "There is no headers in the response"