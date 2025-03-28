<div align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/headerDark.svg" />
    <img src="assets/headerLight.svg" alt="bilitool" />
  </picture>
  <p> </p>

[简体中文](./README.md) | English

`looplive` is a 24/7 automated **multi-platform streaming** tool that theoretically supports any platform with RTMP servers. Feel free to open an [issue](https://github.com/timerring/looplive/issues) to request support for new platforms.

The Python toolkit package and cli designed for auto loop live.

</div>

> Welcome to use looplive! Feedback and PR contributions are appreciated. Please do not use it for purposes that violate community guidelines.

## Features

- Supports 24/7 **automated loop streaming**
- Supports **simultaneous streaming** to multiple platforms: Bilibili, Youtube (more platforms welcome via issues)
- Supports parameter memory, **configure once**, run automatically afterward
- Supports Docker deployment

## Prerequisites

Before using this tool, you need to install ffmpeg:

- Windows: `choco install ffmpeg` (via [Chocolatey](https://chocolatey.org/)) or other methods
- macOS: `brew install ffmpeg` (via [Homebrew](https://brew.sh/))
- Linux: `sudo apt install ffmpeg` (Debian/Ubuntu)

For other operating systems, please refer to the [official website](https://ffmpeg.org/download.html).

Then install looplive:

```bash
pip install looplive
```

## Quick Start

### Start Streaming

#### Bilibili

1. Go to the [live streaming page](https://link.bilibili.com/p/center/index#/my-room/start-live).
   - If you don't have streaming permissions yet, apply first by clicking `Start Live Room` and follow Bilibili's instructions.
2. Click `Start Live`.
3. Get the streaming server URL `-bs` and stream key `-bk` as shown in the image below, just copy them directly.

> To avoid command parameter parsing issues, please wrap each parameter in English double quotes `"`.

![bilibili](https://cdn.jsdelivr.net/gh/timerring/scratchpad2023/2024/2025-03-28-22-06-11.png)

#### Youtube

1. Go to the [live streaming page](https://www.youtube.com/live_dashboard).
3. Get the Stream URL `-ys` and Stream key `-yk`.

> To avoid command parameter parsing issues, please wrap each parameter in English double quotes `"`.

![youtube](https://cdn.jsdelivr.net/gh/timerring/scratchpad2023/2024/2025-03-28-22-13-59.png)

#### Video Folder

**Parameter `-f` is the folder where video files are stored**

> To avoid command parameter parsing issues, please wrap each parameter in English double quotes `"`. You only need to fill in the server_url and key for the platforms you want to use.

```bash
# eg. 
# Configuration for Bilibili only streaming (configure once)
looplive add -bs "rtmp://xxxxxxxx" -bk "?streamname=xxxxxxxx" -f "your/folder/path"
# Configuration for Youtube only streaming (configure once)
looplive add -ys "rtmp://xxxxxxxx" -yk "xxxx-xxxx-xxxx-xxxx-xxxx" -f "your/folder/path"
# Configuration for both Bilibili and Youtube streaming (configure once)
looplive add -bs "rtmp://xxxxxxxx" -bk "?streamname=xxxxxxxx" -ys "rtmp://xxxxxxxx" -yk "xxxx-xxxx-xxxx-xxxx-xxxx" -f "your/folder/path"
```

### Streaming

After configuring parameters once, you can start streaming with these simple commands:

```bash
# Stream to Bilibili only
looplive bili
# Stream to Youtube only
looplive youtube
# Stream to both Bilibili and Youtube
looplive both
```

## Docker Deployment

### Configuration File

The `bili_server_url` and `bili_key` in `config.json` need to be obtained from the [live streaming page](https://link.bilibili.com/p/center/index#/my-room/start-live).

```json
{
    "folder": "/app/looplive/videos",
    "bili_server_url": "rtmp://xxxxxxx",
    "bili_key": "?streamname=xxxxxxxxxxxxxx",
    "youtube_server_url": "rtmp://xxxxxxx", // Set to "" if not needed
    "youtube_key": "xxxx-xxxx-xxxx-xxxx-xxxx" // Set to "" if not needed
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


The Python toolkit package and cli designed for auto loop live.

positional arguments:
  {check,add,reset,bili}
                        Subcommands
    check               Check the configuration
    add                 Add the configuration
    reset              Reset the configuration
    bili               Stream on the bilibili platform

optional arguments:
  -h, --help           show this help message and exit
  -V, --version        Print version information
```