from django.conf.urls import url

from . import views

urlpatterns = [
	url(r"^bidding_list/", views.bidding_list, name='bidding_list'),
	url(r"^add_bidding/", views.add_bidding, name='add_bidding'),
	
]
