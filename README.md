<div align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/headerDark.svg" />
    <img src="assets/headerLight.svg" alt="bilitool" />
  </picture>
  <p> </p>

简体中文 | [English](./README-en.md)

`looplive` 是一个 7 x 24 小时全自动**循环多平台推流**直播工具，理论上只要平台有 rtmp 服务器就能支持，增加新的平台欢迎 [issue](https://github.com/timerring/looplive/issues)。

The Python toolkit package and cli designed for auto loop live.

</div>

> 欢迎使用，欢迎提供更多反馈，欢迎 PR 贡献此项目，请勿用于违反社区规定的用途。

## 特点

- 支持 7 x 24 小时**全自动循环直播**推流
- 支持多平台**同时直播**: Bilibili、Youtube (更多平台欢迎 issue)
- 支持记忆参数，**仅需添加一次**，后续一键自动运行
- 支持 Docker 部署

## 提前准备

使用此工具前，您需要先安装ffmpeg:

- Windows: `choco install ffmpeg`（通过[Chocolatey](https://chocolatey.org/)）或其他方法
- macOS: `brew install ffmpeg`（通过[Homebrew](https://brew.sh/)）
- Linux: `sudo apt install ffmpeg`（Debian/Ubuntu）

更多操作系统安装 ffmpeg 请参考[官方网站](https://ffmpeg.org/download.html)。

然后安装 looplive

```bash
pip install looplive
```

## 快速开始

### 开始直播

#### Bilibili

1. 前往 [直播页面](https://link.bilibili.com/p/center/index#/my-room/start-live).
   - 如果你还没有直播权限，请先申请，点击 `立即开通直播间`，然后按照 b 站提示操作。
2. 点击 `开始直播`.
3. 获取推流服务器地址 `-bs` 和串流密钥 `-bk`，如下图所示，直接复制即可。

> 为了避免命令参数被错误分隔，请使用英文双引号 `"` 包裹每一项参数。

![bilibili](https://cdn.jsdelivr.net/gh/timerring/scratchpad2023/2024/2025-03-28-22-06-11.png)

#### Youtube

1. 前往 [直播页面](https://www.youtube.com/live_dashboard).
3. 获取推流服务器地址(Stream URL) `-ys` 和串流密钥(Stream key) `-yk`。

> 为了避免命令参数被错误分隔，请使用英文双引号 `"` 包裹每一项参数。

![youtube](https://cdn.jsdelivr.net/gh/timerring/scratchpad2023/2024/2025-03-28-22-13-59.png)

#### 视频文件夹

**参数 `-f` 是视频文件的存放文件夹**

> 为了避免命令参数被错误分隔，请使用英文双引号 `"` 包裹每一项参数。可以只填需要的平台对应的 server_url 和 key。

```bash
# eg. 
# 只需要推流到 Bilibili 的配置，只需添加一次
looplive add -bs "rtmp://xxxxxxxx" -bk "?streamname=xxxxxxxx" -f "your/folder/path"
# 只需要推流到 Youtube 的配置，只需添加一次
looplive add -ys "rtmp://xxxxxxxx" -yk "xxxx-xxxx-xxxx-xxxx-xxxx" -f "your/folder/path"
# 同时推流到 Bilibili 和 Youtube 的配置，只需添加一次
looplive add -bs "rtmp://xxxxxxxx" -bk "?streamname=xxxxxxxx" -ys "rtmp://xxxxxxxx" -yk "xxxx-xxxx-xxxx-xxxx-xxxx" -f "your/folder/path"
```

### 推流

只需添加一次参数，以后直接执行以下命令启动即可。

```bash
# 只推流到 Bilibili
looplive bili
# 只推流到 Youtube
looplive youtube
# 同时推流到 Bilibili 和 Youtube
looplive both
```

## Docker 部署

### 配置文件

`config.json` 文件中 `bili_server_url` 和 `bili_key` 需要从 [直播页面](https://link.bilibili.com/p/center/index#/my-room/start-live) 获取。

```json
{
    "folder": "/app/looplive/videos",
    "bili_server_url": "rtmp://xxxxxxx",
    "bili_key": "?streamname=xxxxxxxxxxxxxx",
    "youtube_server_url": "rtmp://xxxxxxx", // 不需要可置为空 ""
    "youtube_key": "xxxx-xxxx-xxxx-xxxx-xxxx" // 不需要可置为空 ""
}
```

### 运行

```bash
sudo docker run -it \
    -v /your/path/to/config.json:/app/looplive/model/config.json \
    -v /your/path/to/videos:/app/looplive/videos \
    --name looplive_docker \
    ghcr.io/timerring/looplive:0.0.1
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