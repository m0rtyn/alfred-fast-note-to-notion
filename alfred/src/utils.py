import json
import os

from cachetools import cached

from notion_api import config


def app_url(browser_url):
    return browser_url.replace("https://", "notion://")
