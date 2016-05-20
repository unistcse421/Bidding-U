from django.conf.urls import url

from . import views

urlpatterns = [
	url(r"^$", views.bidding_list, name='biddinglist'),
	url(r"^addbidding/", views.add_bidding, name='addbidding'),
]
