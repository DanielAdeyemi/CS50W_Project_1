from django.urls import path

from . import views

app_name = 'encyclopedia'
urlpatterns = [
    path("", views.index, name="index"),
    path("error", views.error, name="error"),
    path("add", views.add, name="add"),
    path('edit', views.edit, name='edit'),
    path('random', views.randomEntry, name="random"),
    path("<str:topic>", views.topics, name="topic"),
]
