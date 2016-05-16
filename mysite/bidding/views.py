from django.shortcuts import render

from django.http import HttpResponse

def bidding_list(request):
        return render(request, 'bidding/bidding_list.html', {})

def add_bidding(request):
	return render(request, 'bidding/add_bidding.html', {})
 
# Create your views here.
