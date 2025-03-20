# Copyright (c) 2025 looplive

import subprocess
from looplive.execute.scan_and_execute import scan_folder_and_execute
from looplive.model.model import Model

class BiliController:
    def __init__(self):
        self.model = Model()
        self.server_url = self.model.get_config()['bili_server_url']
        self.key = self.model.get_config()['bili_key']
        self.folder = self.model.get_config()['folder']
    
    @property
    def stream_url(self):
        return f'{self.server_url}{self.key}'

    def stream(self):
        while True:
            scan_folder_and_execute(self.folder, self.stream_url)