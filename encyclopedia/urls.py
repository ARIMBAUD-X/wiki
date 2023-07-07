from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("search/", views.searchPage, name="search"),
    path("<str:title>", views.getPage, name="getPage")
]
