#!/usr/local/bin/python3

import argparse
import sys
from datetime import datetime

from notion_api import notion_api

try:
    parser = argparse.ArgumentParser(description='Add task')
    parser.add_argument('--query', nargs=argparse.REMAINDER, help='query')
    args = parser.parse_args(sys.argv[1].split())

    query = ' '.join(args.query)
    date_time = datetime.now().strftime("%d/%m/%Y, %H:%M")
    query_with_time = query + " @" + date_time

    response = notion_api.append_task_to_notes(query_with_time, True).title
    # print(response, query)
    sys.stdout.write(query)
except Exception as e:
    # Print out nothing on STDOUT (missing value means operation was unsuccessful)
    sys.stdout.write()
