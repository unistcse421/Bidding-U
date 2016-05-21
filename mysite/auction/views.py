from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from auction.models import auction_list
from auction.forms import ItemListForm, AuctionListForm
from django.template import RequestContext

def auction(request):
        all_entries = auction_list.objects.all()
	data = {
		"list_detail" : all_entries
	}	
	print data
	return render_to_response('auction/main.html', data, context_instance = RequestContext(request))
#	return render(request, 'auction/main.html', {})

def add_item(request):
	if(request.method == "POST"):
		edit_form = ItemListForm(request.POST)
		if edit_form.is_valid():
			post = edit_form.save(commit=False)
			post.user_id = '0000'
			post.save()
			edit_form.save_m2m()
		return HttpResponseRedirect('../')
	else:
		edit_form = ItemListForm()
	
	return render(request, 'auction/additem.html', {'form':edit_form,})

def add_auction(request):
        if(request.method == "POST"):
		edit_form = AuctionListForm(request.POST)
                if edit_form.is_valid():
                        post = edit_form.save(commit=False)
                      	post.auction_id = '66'
			post.item_id ='22'
			post.current_price = '33'
			post.book_id = '11'
			post.bidding_state = '0'
			post.save()
			edit_form.save_m2m()
		return HttpResponseRedirect('../')
        else:
		edit_form = AuctionListForm()

	return render(request, 'auction/addauction.html', {'form':edit_form,})


def search(request):
	auction_list.objects
	all_entries = auction_list.objects.all()
	print(all_entries)
