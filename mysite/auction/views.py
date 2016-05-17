from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from auction.forms import ItemListForm, AuctionListForm

# Create your views here.

def auction(request):
	return render(request, 'auction/main.html', {})

def add_item(request):
	if(request.method == "POST"):
		edit_form = ItemListForm(request.POST)
		if edit_form.is_valid():
			post = edit_form.save()
			post.save()
		return HttpResponseRedirect('../')
	else:
		edit_form = ItemListForm()
	
	return render(request, 'auction/additem.html', {'form':edit_form,})

def add_auction(request):
        if(request.method == "POST"):
		edit_form = AuctionListForm(request.POST)
                if edit_form.is_valid():
                        post = edit_form.save()
                        post.save()
		return HttpResponseRedirect('../')
        else:
		edit_form = AuctionListForm()

	return render(request, 'auction/addauction.html', {'form':edit_form,})

#def search_page(request):
#	form = SearchForm()
#	bookname = []

