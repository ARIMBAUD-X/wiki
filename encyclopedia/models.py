from django import forms
from django.db import models
import markdown2
from . import util
# Create your models here.

class wikiPage(models.Model):
    def __init__(self, title):
        entries = util.list_entries()
        if title.capitalize() in entries or title.upper() in entries or title.lower() in entries: # It just works -- T.H. -- for loop = fubar
            self.title = title
        else:
            self.title = False

    def markdownToHtml(self):
        markdown = util.get_entry(self.title)
        match markdown:
            case None | "" | False:
                return f"There is no entry for {self.title}"
            case other:
                return markdown2.markdown(markdown)

"""
    def convertMarkdown(self):
        markdownData = util.get_entry(self.title)
        convertedData = markdown.convert(markdownData)
        self.body = convertedData
"""

