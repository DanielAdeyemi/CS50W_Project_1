from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def topics(request, topic):
    index = 0
    topicsIn = util.list_entries()
    for i, topicIn in enumerate(topicsIn):
        if(topic == topicIn.lower()):
            index = i
    return render(request, "encyclopedia/topic.html", {
        "topic": util.get_entry(topic)
    })
