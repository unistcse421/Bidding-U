# coding: utf-8

from __future__ import unicode_literals

from django import forms

from auction.models import auction_list, success_auction
from mypage.models import item_information

class ItemListForm(forms.ModelForm):
	class Meta:
		model = item_information
		fields = ('user_id', 'book_number', 'reserved_price', 'state',)
	
class AuctionListForm(forms.ModelForm):
        class Meta:
                model = auction_list
                fields = ('item_id', 'due_date', 'book_id', 'current_price', 'bidding_state',)

class SuccessAutionForm(forms.ModelForm):
	class Meta:
		model = success_auction
		fields = ('user_id', 'item_id', 'price',)

class SearchForm(forms.Form):
	query = forms.CharField(
		label = 'search the items',
		widget = forms.TextInput(attrs={'size':32})
	)
