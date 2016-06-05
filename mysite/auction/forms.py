# coding: utf-8

from __future__ import unicode_literals

from django import forms

from auction.models import auction_list, success_auction
from mypage.models import item_information

class ItemListForm(forms.ModelForm):
	class Meta:
		model = item_information
		fields = ('book_number', 'reserved_price', 'state',)

class AuctionListForm(forms.ModelForm):
        class Meta:
                model = auction_list
                fields = ('due_date',)

class SuccessAutionForm(forms.ModelForm):
	class Meta:
		model = success_auction
		fields = ('user_id', 'item_id', 'price', 'winner_id',)

class SearchForm(forms.Form):
	query = forms.CharField(
		label = 'search the items',
		widget = forms.TextInput(attrs={'size':32})
	)
