from django.shortcuts import render, HttpResponse

from . import util, models

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def page(request, title):
    newpage = models.wikiPage(title)
    if newpage.title != False:
        return render(request, "encyclopedia/page.html", {
           "pageData": newpage.body,
           "title": newpage.title
        })
    else:
        print (title)
        return render(request, "encyclopedia/notfound.html",{
            "title": title
        })

def search(request):
    query = request.GET.get("q")
    if query == None or "":
        index(request)
    else:
        searching = models.wikiPage(query)
        if searching.title == False:
            return render(request, "encyclopedia/search.html", {
            "title": query,
            "entries": util.list_entries()
        })
        else:
            page(query)