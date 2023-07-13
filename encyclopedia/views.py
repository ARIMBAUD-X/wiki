from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import wikiPage
from . import util

def index(request):                                             
    return render(request, "encyclopedia/index.html", {         # goto index
        "entries": util.list_entries()
    })

def page(request, title):                                       # attempt to display a new page
    newpage = wikiPage(title)  
    if newpage.title == False:
        return render(request, "encyclopedia/error.html", {
            "title": title,
            "errortype": "notfound"
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

def new(request):
    if request.method =="POST":
        form = request.POST
        if util.get_entry(form["newpagetitle"]) == None:
            util.save_entry(form["newpagetitle"], form["newpagedata"])
            return redirect (f"/wiki/{form['newpagetitle']}")
        elif util.get_entry(form["newpagetitle"]) != None:
            return render(request, "encyclopedia/error.html", {
                "title": form["newpagetitle"],
                "errortype": "pageexists"
            })
    return render(request, "encyclopedia/new.html")

def edit(request, title):
    if request.method == 'POST':
        print (request.POST)
        
        ## append edits
    else: ## here first time
        return render (request, "encyclopedia/edit.html", {
            "title": title,
            "pagedata": util.get_entry(title)
        })

def random(request):
    return render(request, "encyclopedia/random.html")