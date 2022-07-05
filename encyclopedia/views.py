from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from . import util


def index(request):
    # if request.method == 'GET':
    title = request.GET.get('q', '')
    topics = util.list_entries()
    potential_topics = []

    for topic in topics:
        if(title.upper() in topic.upper()):
            potential_topics.append(topic)

    if title:
        if(util.get_entry(title)):
            return render(request, "encyclopedia/topic.html", {
                "topic": util.get_entry(title),
                "header": title.capitalize()
            })
        elif(len(potential_topics)):
            return render(request, "encyclopedia/index.html", {
                "entries": potential_topics
            })
        else:
            return render(request, "encyclopedia/error.html", {
                "param": title
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


def error(request, param):
    return render(request, "encyclopedia/error.html", {
        "param": 'param'
    })
