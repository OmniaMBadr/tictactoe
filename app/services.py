import os

from http import HTTPStatus

import requests


class RandomChoiceService:

    @staticmethod
    def get_choice(choices: list[int]) -> int:
        base_url = os.getenv("RANDOM_CHOICE_SERVICE_URL")
        formated_choices = "&value=".join([str(choice) for choice in choices])
        url = f"{base_url}?value={formated_choices}"
        try:
            response = requests.get(url)
            if response.status_code != HTTPStatus.OK:
                raise Exception("RandomChoiceService: Something wrong with the Random Choice service.")
        except Exception as ex:
            raise Exception(f"RandomChoiceService: Something wrong with the Random Choice service. {ex}")
        else:
            value = response.json().get("value")
            if value and value.isdigit():
                return int(value)
            raise Exception("RandomChoiceService: Invalid choice.")
