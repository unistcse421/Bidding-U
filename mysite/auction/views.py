from django.shortcuts import render
from django.http import HttpResponse

from auction.forms import ItemListForm, AuctionListForm

# Create your views here.

def auction(request):
	edit_form = ItemListForm()
	edit_form2 = AuctionListForm()

	if(request.POST.get('itemadd')):
	        return render(request, 'auction/additem.html', {'form':edit_form,})
	elif(request.POST.get('auctionadd')):
		return render(request, 'auction/addauction.html', {'form':edit_form2,})
	else:
		return render(request, 'auction/main.html', {})

def add_item(request):
	return render(request, 'auction/additem.html', {})

def add_auction(request):

        if(request.method == "POST"):
                return render(request, 'auction/main.html', {'form':edit_form,})
        else:
		return render(request, 'auction/addauction.html', {})


