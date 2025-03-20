# Copyright (c) 2025 autostream

import subprocess
from autostream.execute.scan_and_execute import scan_folder_and_execute

class BiliController:
    def __init__(self, server_url, key, folder):
        self.server_url = server_url
        self.key = key
        self.folder = folder

    @property
    def stream_url(self):
        return f'{self.server_url}{self.key}'

    def stream(self):
        while True:
            scan_folder_and_execute(self.folder, self.stream_url)
