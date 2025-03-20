# autostream

## Prerequisite

In order to use autostream, you have to install the `ffmpeg` library.

Here are some examples:

- Ubuntu

```bash
sudo apt update && apt install ffmpeg -y
```

- MacOS

```bash
brew install ffmpeg
```

- Windows and More: Refer to [the official website](https://www.ffmpeg.org/download.html).

## Usage

### Start the live

1. Go to [the live page](https://link.bilibili.com/p/center/index#/my-room/start-live).
   - If you don't have the live permission, you should apply for it first, click `立即开通直播间`, and then follow the instructions.
2. Click `开始直播`.
3. Get the server url and the key.

### Run the script

```bash
python -m autostream.cli bili --server_url <server_url> --key <key> --folder <folder_path>
```
