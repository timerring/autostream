# looplive

[简体中文](./README.md) | English

> Welcome to `looplive`! We appreciate your feedback and contributions through PRs. Please do not use this project for purposes that violate community guidelines.

`looplive` is a fully automated 24/7 live streaming tool, with plans to support more platforms in the future.

The Python toolkit package and cli designed for auto loop live.

## Prerequisites

First, ensure that you have the `ffmpeg` tool installed on your machine.

- Ubuntu

```bash
sudo apt update && apt install ffmpeg -y
```

- MacOS

```bash
brew install ffmpeg
```

- Windows and other platforms: Please refer to the [official page](https://www.ffmpeg.org/download.html).
- Python >= 3.8

## Usage

### Start Streaming

1. Go to the [live streaming page](https://link.bilibili.com/p/center/index#/my-room/start-live).
   - If you do not have live streaming permissions, please apply first by clicking `Activate Live Room`, and follow the instructions provided by Bilibili.
2. Click `Start Live`.
3. Obtain the streaming server address `-s` and the stream key `-k`.

### Quick Start

> To avoid command parameters being incorrectly separated, please wrap each parameter in English double quotes `"`. The parameter `-f` is the folder where the video files are stored.

```bash
pip install looplive
looplive add -s "rtmp://xxxxxxxx" -k "?streamname=xxxxxxxx" -f "your/folder/path"
looplive bili
```

### More Usage

```bash
$ looplive -h

looplive [-h] [-V] {check,add,reset,bili} ...

The Python toolkit package and cli designed for auto loop live.

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