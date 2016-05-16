from django.shortcuts import render

# Create your views here.

def auction(request):
	return render(request, 'auction/main.html', {})

def add_item(request):
	return render(request, 'auction/additem.html', {})

def add_auction(request):
	return render(request, 'auction/addauction.html', {})


