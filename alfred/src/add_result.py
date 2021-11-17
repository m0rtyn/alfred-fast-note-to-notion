#!/usr/local/bin/python3

import argparse
import sys
import json

from datetime import datetime, date, timedelta
from notion_api import notion_api
from utils import app_url
from notion.collection import NotionDate


try:
    collection = notion_api.get_results_database().collection

    parser = argparse.ArgumentParser(description='Add result')
    parser.add_argument('--query', nargs=argparse.REMAINDER, help='query')
    args = parser.parse_args(sys.argv[1].split())
    tomorrow_date = date.today() + timedelta(days=1)

    query = ' '.join(args.query)

    row = collection.add_row()
    # NOTE: row.name it is notion table column with name "name"
    row.name = query
    row.date = NotionDate(tomorrow_date)

    # Print out alfred-formatted JSON (modifies variables while passing query through)
    output = {
        "alfredworkflow": {
            "arg": query,
            "variables": {
                "url": app_url(row.get_browseable_url())
            }
        }
    }
    print(json.dumps(output))
except Exception as e:
    # Print out nothing on STDOUT (missing value means means operation was unsuccessful)
    sys.stdout.write()