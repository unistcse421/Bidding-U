from django.conf.urls import url

from . import views

urlpatterns = [
        url(r"^$", views.auction, name='auction'),
	url(r"^additem/", views.add_item, name='additem'),
	url(r"^addauction/", views.add_auction, name='addauction'),
]

