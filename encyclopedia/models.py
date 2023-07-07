from django.db import models
from . import util
# Create your models here.

class wikiPage(models.Model):
    def __init__(self, title):
        for pages in util.list_entries():
            if pages.lower == title.lower:
                self.title = pages
                break
            else:
                self.title = False
        self.body = util.get_entry(self.title)