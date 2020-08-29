#!/usr/bin/env -S PATH="${PATH}:/usr/local/bin" python3

from datetime import datetime

from cachetools import cached
from notion.block import CollectionViewBlock, DividerBlock, TextBlock
from notion.client import NotionClient

from notionscripts.config import Config


class NotionApi():
    def __init__(self, config=Config()):
        self.config = config

    @cached(cache={})
    def client(self):
        return NotionClient(token_v2=self.config.notion_token(), monitor=False)

    def get_block(self, id):
        return self.client().get_block(id)

    def append_text_to_block(self, block, text):
        return block.children.add_new(TextBlock, title=text)

    @cached(cache={})
    def notes_page(self):
        return self.client().get_block(self.config.notes_page_url())

    def append_text_to_notes(self, content):
        # Add note to end of the page, then move it to before the divider
        note_block = self.notes_page().children.add_new(TextBlock,
                                                        title=content)
        return note_block
