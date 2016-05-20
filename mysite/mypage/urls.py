from django.conf.urls import url

from . import views

urlpatterns = [
        url(r"^myitem", views.myitem, name='myitem'),
	url(r"^mybidding", views.mybidding, name='mybidding'),
        url(r"^winbidding", views.winbidding, name='winbidding'),
]

