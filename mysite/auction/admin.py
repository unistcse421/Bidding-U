from django.contrib import admin

# Register your models here.

from auction.models import auction_list, success_auction

admin.site.register(auction_list)

admin.site.register(success_auction)
