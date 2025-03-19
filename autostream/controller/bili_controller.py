# Copyright (c) 2025 autostream

import subprocess

class BiliController:
    def __init__(self, server_url, key, file):
        self.server_url = server_url
        self.key = key
        self.file = file

    @property
    def stream_url(self):
        return f'{self.server_url}{self.key}'

    def stream(self):
        command = f'ffmpeg -re -i {self.file} -c copy -f flv "{self.stream_url}"'
        subprocess.run(command, shell=True, check=True)
        # return command
