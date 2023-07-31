from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django import forms
from .models import wikiPage
from random import randint
from . import util


class editForm (forms.Form):
    prepopulatedText = forms.CharField(label='Make your edits', widget=forms.Textarea())

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
        form = editForm(request.POST)
        if form.is_valid():
            newedit = form.cleaned_data['prepopulatedText'] # no longer prepopulated
            newedit = '\r\n'.join([x for x in newedit.splitlines() if x.strip()]) # strips python-added newlines
            util.save_entry(title, newedit)
            return HttpResponseRedirect(f"/wiki/{title}")
    else: ## here first time
        newform = editForm()
        newform.fields['prepopulatedText'].initial = util.get_entry(title)
        return render (request, "encyclopedia/edit.html", {
            "title": title,
            "pagedata": util.get_entry(title),
            "form": newform
        })

def random(request):
    pagelist = util.list_entries()
    a = len(pagelist)
    print (a)
    b = randint(0, a-1) # len is 1-to-n, [b] is 0-to-n
    print (b)
    choice = (pagelist[b])
    print (choice)
    return HttpResponseRedirect(choice)