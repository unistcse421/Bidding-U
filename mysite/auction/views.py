from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def auction(request):
	if(request.GET.get('itemadd')):
	        return render(request, 'auction/additem.html', {})
	else:
		return render(request, 'auction/main.html', {})

def add_item(request):
        if(request.GET.get('add')):
                return render(request, 'auction/main.html', {})
        else:
		return render(request, 'auction/additem.html', {})

def add_auction(request):
        if(request.GET.get('add')):
                return render(request, 'auction/main.html', {})
        else:
		return render(request, 'auction/addauction.html', {})


