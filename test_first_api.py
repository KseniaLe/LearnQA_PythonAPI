import pytest
import requests



class TestFirstApi
    name = [
        ("Vitalii"),
        ("Arseniy"),
        ("")
    ]

    @pytest.mark.parametrize('name',name)
    def Test_hello_call(self):
        url = "https://playground.learnqa.ru/api/hello"
        data = ("name": name)

        response = requests.get(url,params = data)

        assert response.status_code == 200, "Wrong response code"
        