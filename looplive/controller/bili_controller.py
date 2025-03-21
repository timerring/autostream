# Copyright (c) 2025 looplive

import subprocess
from looplive.execute.scan_and_execute import scan_folder_and_execute
from looplive.controller.config_controller import ConfigController

class BiliController:
    def __init__(self, cc: ConfigController):
        self.server_url = cc.get_config()['bili_server_url']
        self.key = cc.get_config()['bili_key']
        self.folder = cc.get_config()['folder']
    
    @property
    def stream_url(self):
        return f'{self.server_url}{self.key}'

    def stream(self):
        while True:
            scan_folder_and_execute(self.folder, self.stream_url)