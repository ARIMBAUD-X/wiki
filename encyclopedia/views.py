from django.shortcuts import render, HttpResponse

from . import util

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
"""
def pageQuery(request, title):
    # SIMPLE TEST FUNC THAT FINDS PAGES; DOES NOT DISPLAY THEM -- NEED A DISPLAY TEMPLATE
    if util.get_entry(title) != None:
        return HttpResponse(title)
    else:
        return HttpResponse("Didn't find it")
"""
def getPage(request, title):
    if util.get_entry(title) != None:
        return render(request, "encyclopedia/page.html", {
           "pageData": util.get_entry(title),
           "title": title
        })
    else:
        return render(request, "encyclopedia/notfound.html",{
            "title": title
        })

def searchPage(request):
    query = request.GET.get("q")
    match query:
        case None | "":                                              # redirect to index
            return render(request, "encyclopedia/index.html",{
                "entries": util.list_entries()
            })
        case _:                                                 # redirect to valid wiki page
            if util.get_entry(query) != None:
                return render(request, "encyclopedia/page.html", {
                "pageData": util.get_entry(query),
                "title": query.upper()
                })
            else:                                               # redirect to search
                return render(request, "encyclopedia/search.html", {
                    "title": query,
                    "entries": util.list_entries()
                })
"""
    if util.get_entry(query) != None:                           # If there is valid wiki contents
        return render(request, "encyclopedia/page.html", {
            "pageData": util.get_entry(query),
            "title": query
        })
    elif query == None:                                         # If the query is blank
        return render(request, "encyclopedia/notfound.html",{
            "title": query
        })
    else:                                                       # If there is a invalid query that is not blank
        return render(request, "encyclopedia/search.html", {
            "title": query,
            "entries": util.list_entries()
        })
"""