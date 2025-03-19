# autostream

## Prerequisite

In order to use autostream, you have to install the ffmpeg library.

Here are some examples:

- Ubuntu

```bash
sudo apt update && apt install ffmpeg -y
```

- CentOS

```bash
sudo yum install epel-release -y \
    && yum update -y \
    && rpm --import http://li.nux.ro/download/nux/RPM-GPG-KEY-nux.ro \
    && rpm -Uvh http://li.nux.ro/download/nux/dextop/el7/x86_64/nux-dextop-release-0-5.el7.nux.noarch.rpm \
    && yum install ffmpeg ffmpeg-devel -y
```

- Windows

```bash
pacman -S mingw-w64-x86_64-ffmpeg
```

- MacOS

```bash
brew install ffmpeg
```

## Usage

### Have the live permission

1. Go to [the live page](https://link.bilibili.com/p/center/index#/my-room/start-live).
2. Click `开始直播`.
3. Get the server url and the key.

### Run the script


```bash
python -m autostream.cli bili --server_url <server_url> --key <key> --file <input_file>
```
