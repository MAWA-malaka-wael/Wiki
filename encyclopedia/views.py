from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
def index(request):
    # This function runs when someone visits the homepage
    # request is information about what the user asked for
    
    entries = ["Python", "HTML", "CSS", "Git", "Django"]
    # This is a list of all encyclopedia entries
    
    return render(request, "encyclopedia/index.html", {
        # This tells Django: take the index.html template and fill it with data
        "entries": entries
        # Send the entries list to the template so it can display them
    })

def entry(request, title):
    return render(request, "encyclopedia/entry.html", {
        "title": title,
        "content": "Content for " + title
    })
def search(request):
    query = request.GET.get("q", "")
    entries = ["Python", "HTML", "CSS", "Git", "Django"]
    results = [e for e in entries if query.lower() in e.lower()]
    return render(request, "encyclopedia/search.html", {
        "query": query,
        "results": results
    })
def new_page(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        entries = ["Python", "HTML", "CSS", "Git", "Django"]
        entries.append(title)
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "content": content
        })
    return render(request, "encyclopedia/new.html", {})
def edit_page(request, title):
    entries = ["Python", "HTML", "CSS", "Git", "Django"]
    if title not in entries:
        return render(request, "encyclopedia/error.html", {})
    if request.method == "POST":
        content = request.POST.get("content")
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "content": content
        })
    return render(request, "encyclopedia/edit.html", {"title": title})
import random

def random_page(request):
    entries = ["Python", "HTML", "CSS", "Git", "Django"]
    title = random.choice(entries)
    return render(request, "encyclopedia/entry.html", {
        "title": title,
        "content": "Content for " + title
    })