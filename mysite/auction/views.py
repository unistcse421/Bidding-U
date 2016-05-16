from django.shortcuts import render

# Create your views here.

def auction(request):
	return render(request, 'auction/main.html', {})
