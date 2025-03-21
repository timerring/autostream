# looplive

[简体中文](./README.md) | English

> Welcome to use, provide more feedback, and contribute to this project via PR. Please do not use it for purposes that violate community regulations.

`looplive` is a 24/7 fully automated looping live streaming tool, expected to support more platforms.

The Python toolkit package and CLI designed for auto loop live.

## Preparation

First, you need to have the `ffmpeg` tool installed on your machine.

- Ubuntu

```bash
sudo apt update && apt install ffmpeg -y
```

- MacOS

```bash
brew install ffmpeg
```

- Windows and more platforms: Please refer to the [official page](https://www.ffmpeg.org/download.html).
- Python >= 3.8

## Quick Start

### Start Live Streaming

1. Go to the [live streaming page](https://link.bilibili.com/p/center/index#/my-room/start-live).
   - If you do not have live streaming permissions, please apply first by clicking `Activate Live Room Now`, and then follow the prompts from Bilibili.
2. Click `Start Live`.
3. Obtain the streaming server address `-s` and stream key `-k`.

### Streaming

> To avoid command parameters being incorrectly separated, please wrap each parameter in English double quotes `"`. The parameter `-f` is the folder where the video files are stored.

```bash
pip install looplive
looplive add -s "rtmp://xxxxxxxx" -k "?streamname=xxxxxxxx" -f "your/folder/path"
looplive bili
```

## Docker Deployment

### Configuration File

The `bili_server_url` and `bili_key` in the `config.json` file need to be obtained from the [live streaming page](https://link.bilibili.com/p/center/index#/my-room/start-live).

```json
{
    "folder": "/app/looplive/videos",
    "bili_server_url": "rtmp://xxxxxxx",
    "bili_key": "?streamname=xxxxxxxxxxxxxx"
}
```

### Running

```bash
sudo docker run -it \
    -v /your/path/to/config.json:/app/looplive/model/config.json \
    -v /your/path/to/videos:/app/looplive/videos \
    --name looplive_docker \
    ghcr.io/timerring/looplive:0.0.1
```

### More Usage

```bash
$ looplive -h

looplive [-h] [-V] {check,add,reset,bili} ...

The Python toolkit package and CLI designed for auto loop live.

positional arguments:
  {check,add,reset,bili}
                        Subcommands
    check               Check the configuration
    add                 Add the configuration
    reset               Reset the configuration
    bili                Stream on the Bilibili platform

optional arguments:
  -h, --help            show this help message and exit
  -V, --version         Print version information
```