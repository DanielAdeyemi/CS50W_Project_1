from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django import forms
from . import util
from re import search, compile


def index(request):
    # if request.method == 'GET':
    title = request.GET.get('q', '')
    topics = util.list_entries()
    potential_topics = []
    p = compile('css')
    if title:
        print((p.search(title)))
        return render(request, "encyclopedia/topic.html", {
            "topic": util.get_entry(title),
            "header": title.capitalize()
        })
        if prin in 'css':
            return render(request, "encyclopedia/topic.html", {
                "topic": util.get_entry('css'),
                "header": 'css'.capitalize()
            })
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def topics(request, topic):
    if request.method == 'GET':
        if(util.get_entry(topic)):
            return render(request, "encyclopedia/topic.html", {
                "topic": util.get_entry(topic),
                "header": topic.capitalize()
            })
        else:
            return render(request, "encyclopedia/error.html")


def error(request):
    return render(request, "encyclopedia/error.html")
