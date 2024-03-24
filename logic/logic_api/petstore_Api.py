import json

import requests
from infra.api_wrapper import APIWrapper


class PetStore:

    def __init__(self, api_object, url):
        self.my_api = api_object
        self.api_wrapper = APIWrapper()
        self.base_url = url

    def Add_Cart_api_json(self, headers, payload):
        url = f'{self.base_url}cart/add'
        response = self.my_api.api_post_request(url, headers=headers, data=payload)
        return response.json()

    def get_Cart_quantity(self):
        url = f'{self.base_url}cart/add'
        response = self.my_api.api_get_request(url)
        return response

    def main(self):
        json_response = self.Add_Cart_api_json()
        print(json_response)


if __name__ == "__main__":
    api_wrapper = APIWrapper()
    pet_store = PetStore(api_wrapper)
    pet_store.main()
