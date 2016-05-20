from django.shortcuts import render

# Create your views here.

def myitem(request):
	return render(request, 'mypage/myitem.html', {})

def mybidding(request):
        return render(request, 'mypage/mybidding.html', {})

def winbidding(request):
        return render(request, 'mypage/winbidding.html', {})


