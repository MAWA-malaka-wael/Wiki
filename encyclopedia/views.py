from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
import markdown2
import random

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entry(request, title):
    content = util.get_entry(title)
    if content is None:
        return render(request, "encyclopedia/error.html", {
            "title": title
        })
    return render(request, "encyclopedia/entry.html", {
        "title": title,
        "content": markdown2.markdown(content)
    })


def search(request):
    query = request.GET.get("q", "")
    entries = util.list_entries()
    if query in entries:
        return HttpResponseRedirect(reverse("entry", args=[query]))
    results = [e for e in entries if query.lower() in e.lower()]
    return render(request, "encyclopedia/search.html", {
        "query": query,
        "results": results
    })


def new_page(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        entries = util.list_entries()
        if title in entries:
            return render(request, "encyclopedia/new.html", {
                "error": "An entry with this title already exists."
            })
        util.save_entry(title, content)
        return HttpResponseRedirect(reverse("entry", args=[title]))
    return render(request, "encyclopedia/new.html", {})


def edit_page(request, title):
    if request.method == "POST":
        content = request.POST.get("content")
        util.save_entry(title, content)
        return HttpResponseRedirect(reverse("entry", args=[title]))
    content = util.get_entry(title)
    return render(request, "encyclopedia/edit.html", {
        "title": title,
        "content": content
    })


def random_page(request):
    entries = util.list_entries()
    title = random.choice(entries)
    return HttpResponseRedirect(reverse("entry", args=[title]))