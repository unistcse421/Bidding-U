#coding : utf - 8

from __future__ import unicode_literals

from django import forms 

from bidding.models import candidate_list 

class CandidateListForm(forms.ModelForm):
	class Met:
		model = candidate_list
		fileds = ('suggest_price',)
