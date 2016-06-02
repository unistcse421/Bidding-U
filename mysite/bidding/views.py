from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from bidding.models import candidate_list
from auction.models import auction_list
from bidding.forms import CandidateListForm
from django.template import RequestContext

def bidding_list(request, auction_id):
	all_entries = candidate_list.objects.all().order_by('suggest_time').reverse()
	data = {
		"list_detail" : all_entries
	}
	print data
        return render_to_response('bidding/bidding_list.html', data, context_instance = RequestContext(request))

def add_bidding(request, auction_id):
	entriy = auction_list.objects.get(auction_id = auction_id)
	data = {
		"item_detail" : entriy
	}
        if(request.method == "POST"):
                edit_form = CandidateListForm(request.POST)
                if edit_form.is_valid():
                        post = edit_form.save(commit=False)
                        post.user_id = '0000'
                        post.auction_id = auction_id
                        post.save()
                        edit_form.save_m2m()
                return HttpResponseRedirect('../')
        else:
                edit_form = CandidateListForm()
     
	print data
	render_to_response('bidding/add_bidding.html', data, context_instance = RequestContext(request))
	return render(request, 'bidding/add_bidding.html', {'form':edit_form,})

