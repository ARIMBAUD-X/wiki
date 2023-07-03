from django.shortcuts import render, HttpResponse

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def pageQuery(request, title):
    # SIMPLE TEST FUNC THAT FINDS PAGES; DOES NOT DISPLAY THEM -- NEED A DISPLAY TEMPLATE
    if util.get_entry(title) != None:
        return HttpResponse(title)
    else:
        return HttpResponse("Didn't find it")