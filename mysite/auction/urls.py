from django.conf.urls import url

from . import views

surlpatterns = [
        url(r"^$", views.index, name='auction'),
]

