from django.conf.urls import url

from . import views

urlpatterns = [
	url(r"^(?P<auction_id>[0-9]+)/$", views.bidding_list, name='biddinglist'),
	url(r"^(?P<auction_id>[0-9]+)/addbidding/$", views.add_bidding, name='addbidding'),
	url(r"^(?P<item_id>[0-9]+)/$", views.bidding_list, name='biddinglist'),
]
