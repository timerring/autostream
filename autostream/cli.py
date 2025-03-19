# Copyright (c) 2025 autostream

import argparse
import sys
import os
import logging
from autostream.controller.bili_controller import BiliController


def cli():
    parser = argparse.ArgumentParser(description='The Python toolkit package and cli designed for auto streaming')
    parser.add_argument('-V', '--version', action='version', version='autostream 0.0.1', help='Print version information')

    subparsers = parser.add_subparsers(dest='subcommand', help='Subcommands')

    # Bilibili stream
    bilibili_parser = subparsers.add_parser('bili', help='Stream on Bilibili')
    bilibili_parser.add_argument('--server_url', required=True, help='(required) The server url')
    bilibili_parser.add_argument('--key', required=True, help='(required) The stream key')
    bilibili_parser.add_argument('--file', required=True, help='(required) The input file')

    args = parser.parse_args()

    # Check if no subcommand is provided
    if args.subcommand is None:
        print("No subcommand provided. Please specify a subcommand.")
        parser.print_help()
        sys.exit()

    if args.subcommand == 'bili':
        print(args)
        BiliController(args.server_url, args.key, args.file).stream()

if __name__ == '__main__':
    cli()