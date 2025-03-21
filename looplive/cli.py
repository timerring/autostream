# Copyright (c) 2025 looplive

import argparse
import sys
import os
import logging
from looplive.controller.bili_controller import BiliController
from looplive.controller.config_controller import ConfigController


def cli():
    parser = argparse.ArgumentParser(description='The Python toolkit package and cli designed for auto loop live.')
    parser.add_argument('-V', '--version', action='version', version='looplive 0.0.1', help='Print version information')

    subparsers = parser.add_subparsers(dest='subcommand', help='Subcommands')

    # Check config
    check_config_parser = subparsers.add_parser('check', help='Check the configuration')

    # Add config
    add_config_parser = subparsers.add_parser('add', help='Add the configuration')
    add_config_parser.add_argument('-s', '--bili_server_url', help='The bilibili server url')
    add_config_parser.add_argument('-k', '--bili_key', help='The bilibili stream key')
    add_config_parser.add_argument('-f', '--folder', help='The input folder')

    # Reset config
    reset_config_parser = subparsers.add_parser('reset', help='Reset the configuration')

    # Bilibili stream
    bilibili_parser = subparsers.add_parser('bili', help='Stream on the bilibili platform')

    args = parser.parse_args()

    # Check if no subcommand is provided
    if args.subcommand is None:
        print("No subcommand provided. Please specify a subcommand.")
        parser.print_help()
        sys.exit()

    if args.subcommand == 'check':
        ConfigController().check_config()
        print(ConfigController().get_config())

    if args.subcommand == 'add':
        if args.bili_server_url:
            ConfigController().update_specific_config('bili_server_url', args.bili_server_url)
        if args.bili_key:
            ConfigController().update_specific_config('bili_key', args.bili_key)
        if args.folder:
            ConfigController().update_specific_config('folder', args.folder)

    if args.subcommand == 'reset':
        ConfigController().reset_config()

    if args.subcommand == 'bili':
        cc = ConfigController()
        if cc.check_config():
            BiliController(cc).stream()
        else:
            print("Please complete the configuration first!", flush=True)

if __name__ == '__main__':
    cli()