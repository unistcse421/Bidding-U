from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from mypage.models import item_information
from auction.models import auction_list, success_auction
from bidding.models import candidate_list
from django.template import RequestContext
from mysite.models import user_profile

# Create your views here.

def myitem(request):
	current_user = request.user
        all_entries = item_information.objects.filter(user_id=current_user.id)
        data = {
                "list_detail" : all_entries
        }
        print data
        return render_to_response('mypage/myitem.html', data, context_instance = RequestContext(request))


def mybidding(request):
	current_user = request.user
        all_entries = candidate_list.objects.filter(user_id=current_user.id)
        data = {
                "list_detail" : all_entries
        }
        print data
        return render_to_response('mypage/mybidding.html', data, context_instance = RequestContext(request))


def winbidding(request):
	current_user = request.user
        all_entries = success_auction.objects.filter(user_id=current_user.id)
        data = {
                "list_detail" : all_entries
        }
        print data
        return render_to_response('mypage/winbidding.html', data, context_instance = RequestContext(request))



