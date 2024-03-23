import json
import os


class ConfigHandler:
    def __init__(self, config_file_path):
        self.config_file_path = os.getenv('C:/Users/odehm/Desktop/repos/petsore/config.json')
        self.config = self.load_config(config_file_path)

    def load_config(self, config_file_path):
        with open(config_file_path, 'r') as f:
            return json.load(f)

    def get_config_value(self, key):
        return self.config.get(key)
