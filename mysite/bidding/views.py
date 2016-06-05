from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from bidding.models import candidate_list
from auction.models import auction_list
from mypage.models import item_information
from bidding.forms import CandidateListForm
from django.template import RequestContext
from mysite.models import user_profile

def bidding_list(request, auction_id):
	auction = auction_list.objects.get(auction_id = auction_id)
	item = item_information.objects.get(item_id = auction.item_id)
	#name = user_profile.objects.get(user_id = item.user_id)

	entries = candidate_list.objects.filter(auction_id = auction_id).order_by('suggest_time').reverse()

	data = {
		"list_detail" : entries,
		"auction_info" : auction,
		"item_info" : item,
	}

	if(auction.bidding_state == False):
        	return render_to_response('bidding/bidding_list_finished.html',data, context_instance = RequestContext(request))
	else:
		if(request.user.id == item.user_id):
        		return render_to_response('bidding/bidding_list_my.html',data, context_instance = RequestContext(request))
		else:
        		return render_to_response('bidding/bidding_list.html', data, context_instance = RequestContext(request))


def add_bidding(request, auction_id):
	entry = auction_list.objects.get(auction_id = auction_id)
        if(request.method == "POST"):
                edit_form = CandidateListForm(request.POST)
                if edit_form.is_valid():
                	post = edit_form.save(commit=False)
			if(post.suggest_price <= entry.current_price):
				edit_form = CandidateListForm()
			        return render_to_response('bidding/add_bidding.html', {'error':'Higer than current price', 'data':entry,'form':edit_form,}, context_instance = RequestContext(request))

			else:
                        	post.user_id = request.user.id
                        	post.auction_id = auction_id
                        	post.save()
				entry.current_price = post.suggest_price
				entry.expected_winner = request.user.id
				entry.save()
                        	edit_form.save_m2m()
                		return HttpResponseRedirect('../')
        else:
                edit_form = CandidateListForm()
    
	return render_to_response('bidding/add_bidding.html', {'data':entry,'form':edit_form,}, context_instance = RequestContext(request))

