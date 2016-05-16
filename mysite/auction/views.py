from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def auction(request):
	return render(request, 'auction/main.html', {})
