from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django import forms
from . import util


def index(request):
    if request.method == 'GET':
        prin = request.GET.get('q')
        return render(request, "encyclopedia/topic.html", {
            "topic": util.get_entry(prin),
            "header": prin.capitalize()
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
