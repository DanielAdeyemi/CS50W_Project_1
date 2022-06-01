from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def topics(request, topic):
    if(util.get_entry(topic)):
        return render(request, "encyclopedia/topic.html", {
            "topic": util.get_entry(topic),
            "header": topic.capitalize()
        })
    else:
        return render(request, "encyclopedia/error.html")
