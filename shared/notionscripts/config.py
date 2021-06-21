#!/usr/bin/env -S PATH="${PATH}:/usr/local/bin" python3

import os

from cachetools import cached


class Config():
    @cached(cache={})
    def notion_token(self):
        return os.environ.get('NOTION_TOKEN')
