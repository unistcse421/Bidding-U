from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from auction.models import auction_list
from mypage.models import item_information
from auction.forms import ItemListForm, AuctionListForm
from django.template import RequestContext

def auction(request):
        all_entries = auction_list.objects.all().reverse()
	data = {
		"list_detail" : all_entries
	}	
	print data
	return render_to_response('auction/main.html', data, context_instance = RequestContext(request))

def add_item(request):
	if(request.method == "POST"):
		edit_form = ItemListForm(request.POST)
		if edit_form.is_valid():
			post = edit_form.save(commit=False)
			post.user_id = '0000'
			post.save()
			edit_form.save_m2m()
		return HttpResponseRedirect('../../../mypage/myitem')
	else:
		edit_form = ItemListForm()
	
	return render(request, 'auction/additem.html', {'form':edit_form,})

def add_auction(request, item_id):
        if(request.method == "POST"):
		edit_form = AuctionListForm(request.POST)
		item_entries = item_information.objects.get(item_id = item_id)
       		data = {
			"list_detail" : item_entries
		} 
		if edit_form.is_valid():
                        post = edit_form.save(commit=False)                     
			post.item_id = item_id
			post.current_price = item_entries.reserved_price
			post.book_id = item_entries.book_number
			post.save()
			item_entries.on_going = True
			item_entries.save()
			edit_form.save_m2m()
		return HttpResponseRedirect('../../')
        else:
		edit_form = AuctionListForm()

	return render(request, 'auction/addauction.html', {'form':edit_form,})


def search(request):
	auction_list.objects
	all_entries = auction_list.objects.all()
	print(all_entries)
