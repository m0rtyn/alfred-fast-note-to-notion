#!/usr/local/bin/python3

import argparse
import sys

from notion_api import notion_api

try:
    parser = argparse.ArgumentParser(description='Add note')
    parser.add_argument('--query', nargs=argparse.REMAINDER, help='query')
    args = parser.parse_args(sys.argv[1].split())

    query = ' '.join(args.query)
    response = notion_api.append_text_to_notes(query).title

    sys.stdout.write(query)
except Exception as e:
    # Print out nothing on STDOUT (missing value means means operation was unsuccessful)
    sys.stdout.write()
    # sys.stderr.write('Error!')
