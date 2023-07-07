from django.shortcuts import render
from .models import wikiPage
from . import util

def index(request):                                             
    return render(request, "encyclopedia/index.html", {         # goto index
        "entries": util.list_entries()
    })

def page(request, title):                                       # attempt to display a new page
    newpage = wikiPage(title)  
    if newpage.title == False:
        return render(request, "encyclopedia/notfound.html", {
            "title": title
        })           
    else:
        return render(request, "encyclopedia/page.html", {
            "pageData": newpage.markdownToHtml,
            "title": newpage.title
        })               # 
""" 
if newpage.title != False:
        return render(request, "encyclopedia/page.html", {
           "pageData": newpage.body,
           "title": newpage.title
        })
    elif newpage.title == False:
        return render(request, "encyclopedia/notfound.html",{
            "title": title
        })
"""

def search(request):
    query = request.GET.get("q")
    # converts when it should not
    """if blank go to index
    if not blank but not an entry, go to search
    else if not blank and an entry, go to entry"""
    if query == None or query == "" or query == False:
        return index(request)
    elif util.get_entry(query) == None:  # must be false, not none
        """searchingPage = wikiPage(query)
        match searchingPage.title:
            case False, None, "": ## catch error?
                return index(request)
            case other:"""
        return render (request, "encyclopedia/search.html",{
            "title": query,
            "entries": util.list_entries()
        })
    else:
        return page(request, query) # doesnt quite redirect?
        """if searchingPage.title == False or :
            return render(request, "encyclopedia/search.html", {
            "title": query,
            "entries": util.list_entries()
        })"""