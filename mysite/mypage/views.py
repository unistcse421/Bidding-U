from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from mypage.models import item_information
from auction.models import auction_list, success_auction
from bidding.models import candidate_list
from django.template import RequestContext


# Create your views here.

def myitem(request):
        all_entries = item_information.objects.all()
        data = {
                "list_detail" : all_entries
        }
        print data
        return render_to_response('mypage/myitem.html', data, context_instance = RequestContext(request))


def mybidding(request):
        all_entries = candidate_list.objects.all()
        data = {
                "list_detail" : all_entries
        }
        print data
        return render_to_response('mypage/mybidding.html', data, context_instance = RequestContext(request))


def winbidding(request):
        all_entries = success_auction.objects.all()
        data = {
                "list_detail" : all_entries
        }
        print data
        return render_to_response('mypage/winbidding.html', data, context_instance = RequestContext(request))



