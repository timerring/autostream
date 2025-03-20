# Copyright (c) 2025 looplive

import json
import os

class Model:
    def __init__(self, path=None) -> None:
        if path is None:
            self.path = os.path.join(os.path.dirname(__file__), "config.json")
        else:
            self.path = path
        self.default_config = {
            "folder": "",
            "bili_server_url": "",
            "bili_key": ""
        }

    def get_default_config(self):
        return self.default_config

    def reset_config(self):
        self.write(self.default_config)

    def update_specific_config(self, key, value):
        config_info = self.get_config()
        config_info[key] = value
        self.write(config_info)
    
    def update_multiple_config(self, updates: dict):
        config_info = self.get_config()
        for key, value in updates.items():
            config_info[key] = value
        self.write(config_info)

    def get_config(self):
        if not os.path.exists(self.path):
            self.reset_config()
        return self.read()

    def read(self):
        with open(self.path, "r") as f:
            return json.load(f)

    def write(self, config):
        with open(self.path, "w") as f:
            json.dump(config, f, indent=4)
