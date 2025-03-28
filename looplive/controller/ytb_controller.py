# Copyright (c) 2025 looplive

import subprocess
from looplive.execute.scan_and_execute import scan_folder_and_execute
from looplive.controller.config_controller import ConfigController

class YtbController:
    def __init__(self, cc: ConfigController):
        self.server_url = cc.get_config()['ytb_server_url']
        self.key = cc.get_config()['ytb_key']
        self.folder = cc.get_config()['folder']
    
    @property
    def stream_url(self):
        # Add leading slash to key if it doesn't start with one
        key = self.key if self.key.startswith('/') else f'/{self.key}'
        return f'{self.server_url}{key}'

    def stream(self):
        while True:
            scan_folder_and_execute(self.folder, self.stream_url)