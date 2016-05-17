from django.shortcuts import render
from django.http import HttpResponse

from auction.forms import ItemListForm, AuctionListForm

# Create your views here.

def auction(request):
	#edit_form = ItemListForm()
	#edit_form2 = AuctionListForm()

#if(request.POST.get('itemadd')):
#	        return render(request, 'auction/additem.html', {'form':edit_form})
#		return render(request, 'auction/additem.html',{})
#	elif(request.POST.get('auctionadd')):
#		return render(request, 'auction/addauction.html', {'form':edit_form2,})
	
	return render(request, 'auction/main.html', {})

def add_item(request):

	if(request.method == "POST"):
		edit_form = ItemListForm(request.POST)
		if edit_form.is_valid():
			post = edit_form.save()
			post.save()
		return render(request, 'auction/main.html', {'form':edit_form,})
#		return redirect('auction/main.html', pk=post.pk)
	else:
		edit_form = ItemListForm()
		return render(request, 'auction/additem.html', {'form':edit_form,})

def add_auction(request):

        if(request.method == "POST"):
		edit_form = AuctionListForm()
                if edit_form.is_valid():
                        post = edit_form.save()
                        post.save()
		return render(request, 'auction/main.html', {'form':edit_form,})
        else:
		edit_form = AuctionListForm()
		return render(request, 'auction/addauction.html', {'form':edit_form})


