from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from auction.models import auction_list, success_auction
from mypage.models import item_information
from auction.forms import ItemListForm, AuctionListForm
from django.template import RequestContext
from mysite.models import user_profile
import datetime

def auction(request):
	close_auction(request)
        all_entries = auction_list.objects.all().order_by('due_date')
	
	data = {
		"ongoing_detail" : all_entries.filter(bidding_state = True),
		"finish_detail" : all_entries.filter(bidding_state = False)
	}	

	return render_to_response('auction/main.html', data, context_instance = RequestContext(request))

def add_item(request):
        current_user = request.user.id

	if(request.method == "POST"):
		edit_form = ItemListForm(request.POST)
		if edit_form.is_valid():
			post = edit_form.save(commit=False)
			post.user_id = current_user
			post.save()
			edit_form.save_m2m()
		return HttpResponseRedirect('../../../mypage/myitem')
	else:
		edit_form = ItemListForm()
	
	return render(request, 'auction/additem.html', {'form':edit_form,})

def add_auction(request, item_id):
        if(request.method == "POST"):
		edit_form = AuctionListForm(request.POST)
		item_entry = item_information.objects.get(item_id = item_id)
       		data = {
			"list_detail" : item_entry
		} 
		if edit_form.is_valid():
                        post = edit_form.save(commit=False)                     
			post.item_id = item_id
			post.current_price = item_entry.reserved_price
			post.book_name= item_entry.book_name
			post.expected_winner = request.user.id
			post.save()
			item_entry.on_going = 1
			item_entry.save()
			edit_form.save_m2m()
		return HttpResponseRedirect('../../')
        else:
		edit_form = AuctionListForm()

	return render(request, 'auction/addauction.html', {'form':edit_form,})

def close_auction(request):
	now = datetime.datetime.now()
	past_entries = auction_list.objects.filter(due_date__lte = now)

	for past in past_entries:
		if(past.bidding_state == True):
			past.bidding_state = False
			past.save()
			item = item_information.objects.get(item_id = past.item_id)		
			seller = user_profile.objects.get(id = item.user_id)
			win = success_auction.objects.create(item_id = past.item_id, user_id = past.user_id, price = past.current_price, winner_id = past.expected_winner)
			win.save(force_insert = True)
	

def search(request):
	auction_list.objects
	all_entries = auction_list.objects.all()
	print(all_entries)
