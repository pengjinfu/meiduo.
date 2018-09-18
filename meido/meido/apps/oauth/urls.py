from django.conf.urls import url
from django.contrib import admin
from . import views
urlpatterns = [
    url(r'^qq/authorization/$', views.QQLoginURLView.as_view()),
    url(r'^qq/user/$', views.QQLoginView.as_view()),
]
