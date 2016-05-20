from django.conf.urls import url

from . import views

urlpatterns = [
        url(r"^$", views.auction, name='auction'),
	url(r"^itemadd/", views.add_item, name='additem'),
	url(r"^auctionadd/", views.add_auction, name='addauction'),
]
