import json
import os
import sys
from pathlib import Path

from cachetools import cached


class Config():
    @cached(cache={})
    def config_file_path(self):
        return str(
            Path(__file__).parent.parent.absolute()) + "/data/config.json"

    @cached(cache={})
    def config_json(self):
        try:
            if os.path.isfile(self.config_file_path()):
                with open(self.config_file_path()) as json_file:
                    return json.load(json_file)
        except Exception as e:
            # Print out nothing on STDOUT (missing value means means operation was unsuccessful)
            sys.stderr.write(e)

    @cached(cache={})
    def notion_token(self):
        return self.config_json()['NOTION_TOKEN']

    @cached(cache={})
    def notes_page_url(self):
        return self.config_json()['NOTES_PAGE_URL']
