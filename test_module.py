import pytest
from main import Client


class TestModule:
    def setup_method(self):
        self.client = Client(klic="klic")


    @pytest.mark.parametrize("input,expected", [ 
        ("Adelaida", ["paní Adelaido"]),
        ("Adelaida|Tomáš Novák", ["paní Adelaido", "pane Nováku"])
    ])
    def test_request(self, input, expected):
        test_result = self.client.request(jmeno=input)
        assert test_result == expected


    @pytest.mark.parametrize("input,expected", [
        ("", ["5"])
    ])
    def test_error_messages(self, input, expected):
        test_result = self.client.request(jmeno=input)
        assert test_result == expected


    @pytest.mark.parametrize("input,expected", [
        (None, list)
    ])
    def test_account_info(self, input, expected):
        test_result = self.client.account_info(input)
        assert type(test_result) == expected