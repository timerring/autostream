# Copyright (c) 2025 autostream

from autostream.model.model import Model

class ConfigController:
    def __init__(self):
        self.model = Model()
        
    def check_config(self):
        config_info = self.model.get_config()
        if not config_info['bili_server_url'] or not config_info['bili_key'] or not config_info['folder']:
            print("The configuration is not complete!", flush=True)
            return False
        return True

    def update_config(self, config_info):
        self.model.update_multiple_config(config_info)

    def reset_config(self):
        self.model.reset_config()

    def get_config(self):
        return self.model.get_config()

    def get_specific_config(self, key):
        return self.model.get_specific_config(key)

    def update_specific_config(self, key, value):
        self.model.update_specific_config(key, value)
