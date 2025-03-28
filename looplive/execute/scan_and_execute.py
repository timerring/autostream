# Copyright (c) 2025 looplive

import os
import subprocess

def scan_folder_and_execute(folder_path, stream_url):
    files = sorted(os.listdir(folder_path))
    for file in files:
        if file.lower().endswith(('.flv', '.mp4')):
            file_path = os.path.join(folder_path, file)
            if os.path.isfile(file_path):
                command = f'ffmpeg -re -i {file_path} -c copy -f flv "{stream_url}"'
                subprocess.run(command, shell=True, check=True)