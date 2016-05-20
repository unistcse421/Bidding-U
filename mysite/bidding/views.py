from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from bidding.forms import CandidateListForm

def bidding_list(request):
        return render(request, 'bidding/bidding_list.html', {})

def add_bidding(request):
        if(request.method == "POST"):
                edit_form = CandidateListForm(request.POST)
                if edit_form.is_valid():
                        post = edit_form.save(commit=False)
                        post.user_id = '0000'
                        post.auction_id = '0000'
	#		post.suggest_time = '0000'
                        post.save()
                        edit_form.save_m2m()
                return HttpResponseRedirect('../')
        else:
                edit_form = CandidateListForm()
      
	return render(request, 'bidding/add_bidding.html', {'form':edit_form,})

