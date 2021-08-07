import requests



class TestGetCookie:
     def test_get_cookie(self):
          url = "https://playground.learnqa.ru/api/homework_cookie"
          response = requests.get(url)
          cookie_value = response.cookies
          print(cookie_value)

          assert cookie_value != None, "There is no cookie in the response"




