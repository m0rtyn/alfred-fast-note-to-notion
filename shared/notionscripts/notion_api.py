#!/usr/bin/env -S PATH="${PATH}:/usr/local/bin" python3

from cachetools import cached
from notion.block import TextBlock, TodoBlock
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
        note_block = self.notes_page().children.add_new(TextBlock,
                                                        title=content)
        return note_block

    def append_task_to_notes(self, content, checked):
        task_block = self.notes_page().children.add_new(TodoBlock, title=content, checked=checked)
        
        return task_block
