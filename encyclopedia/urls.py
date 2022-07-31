from django.urls import path

from . import views

app_name = 'encyclopedia'
urlpatterns = [
    path("", views.index, name="index"),
    path("<str:topic>", views.topics, name="topic"),
    path("error", views.error, name="error"),
    path("add", views.add, name="add"),
]
