import os

from http import HTTPStatus
import unittest
from unittest.mock import patch

import requests

from app.services import RandomChoiceService


class TestRandomChoiceService(unittest.TestCase):

    def test_get_choice_successfully(self):
        response = requests.Response()
        response.status_code = HTTPStatus.OK
        response._content = b'{"value": "5"}'
        choices = [1, 5, 7]
        with patch("requests.get", return_value=response) as request:
            choice = RandomChoiceService.get_choice(choices=choices)
            self.assertEqual(choice, 5)
            request.assert_called_with(f'{os.getenv("RANDOM_CHOICE_SERVICE_URL")}?value=1&value=5&value=7')
