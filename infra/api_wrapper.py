import requests

from infra.config_handler import ConfigHandler


class APIWrapper:
    def __init__(self):
        self.response = None
        self.my_request = requests

    def api_get_request(self, url_api):
        self.response = self.my_request.get(url_api)
        if self.response.ok:
            return self.response
        else:
            return self.response.status_code

    def api_post_request(self, url, headers, data):
        self.response = self.my_request.post(url, headers=headers, data=data)
        if self.response.ok:
            return self.response
        else:
            return self.response.status_code
