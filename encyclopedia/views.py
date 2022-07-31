from cProfile import label
from multiprocessing import context
from pydoc import describe
from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from . import util


class NewTopicForm(forms.Form):
    topic = forms.CharField(label='New Topic')
    text = forms.CharField(label='Description', widget=forms.Textarea())


class EditTopicForm(forms.Form):
    topic = forms.CharField(label="Edit topic")
    text = forms.CharField(label='Edit Description', widget=forms.Textarea())


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
        # else:
        #     return render(request, "encyclopedia/add.html", {
        #         'form': NewTopicForm})
    elif request.method == 'POST':
        form = NewTopicForm(request.POST)
        if form.is_valid():
            topic = form.cleaned_data['topic']
            description = form.cleaned_data['text']
            mdEntry = '# ' + topic + '\n' + '\n' + description
            if util.get_entry(topic):
                return render(request, "encyclopedia/error.html")
            else:
                util.save_entry(topic, mdEntry)
                return render(request, "encyclopedia/topic.html", {
                    "topic": mdEntry,
                    "header": topic.capitalize()
                })
        else:
            return render(request, 'encyclopedia/add.html', {
                'form': form
            })
    return render(request, 'encyclopedia/add.html', {
        'form': NewTopicForm
    })


def edit(request):
    context = {}
    topic = request.GET.get('topic')
    description = util.get_entry(topic)
    initial_params = {
        'topic': topic,
        'text': description
    }
    form = EditTopicForm(request.POST or None, initial=initial_params)
    context['form'] = form
    if request.method == "GET":
        return render(request, 'encyclopedia/edit.html', context)
    elif request.method == 'POST':
        if form.is_valid():
            topic = form.cleaned_data['topic']
            description = form.cleaned_data['text']
            util.save_entry(topic, description)
            return render(request, "encyclopedia/topic.html", {
                "topic": description,
                "header": topic.capitalize()
            })


def error(request, param):
    return render(request, "encyclopedia/error.html", {
        "param": 'param'
    })


def add(request):
    if request.method == 'POST':
        form = NewTopicForm(request.POST)
        if form.is_valid():
            topic = form.cleaned_data['topic']
            description = form.cleaned_data['text']
            mdEntry = '# ' + topic + '\n' + '\n' + description
            if util.get_entry(topic):
                return render(request, "encyclopedia/error.html")
            else:
                util.save_entry(topic, mdEntry)
                return render(request, "encyclopedia/topic.html", {
                    "topic": mdEntry,
                    "header": topic.capitalize()
                })
        else:
            return render(request, 'encyclopedia/add.html', {
                'form': form
            })
    return render(request, "encyclopedia/add.html", {
        'form': NewTopicForm})
