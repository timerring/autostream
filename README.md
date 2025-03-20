# looplive

简体中文 | [English](./README-en.md)

> 欢迎使用，欢迎提供更多反馈，欢迎 PR 贡献此项目，请勿用于违反社区规定的用途。

`looplive` 是一个 7 x 24 小时全自动循环推流直播工具，预计支持更多的平台。

The Python toolkit package and cli designed for auto loop live.

## 提前准备

首先，你的机器上需要有 `ffmpeg` 工具。

- Ubuntu

```bash
sudo apt update && apt install ffmpeg -y
```

- MacOS

```bash
brew install ffmpeg
```

- Windows 和更多平台: 请参考 [官方页面](https://www.ffmpeg.org/download.html).
- Python >= 3.8

## 使用

### 开始直播

1. 前往 [直播页面](https://link.bilibili.com/p/center/index#/my-room/start-live).
   - 如果你还没有直播权限，请先申请，点击 `立即开通直播间`，然后按照 b 站提示操作。
2. 点击 `开始直播`.
3. 获取推流服务器地址 `-s` 和串流密钥 `-k`。

### 快速开始

> 为了避免命令参数被错误分隔，请使用英文双引号 `"` 包裹每一项参数。参数 `-f` 是视频文件的存放文件夹。

```bash
looplive add -s "rtmp://xxxxxxxx" -k "?streamname=xxxxxxxx" -f "your/folder/path"
looplive bili
```

### 更多用法

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
    bili                Stream on the bilibili platform

optional arguments:
  -h, --help            show this help message and exit
  -V, --version         Print version information
```