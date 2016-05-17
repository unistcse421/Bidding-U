from django.contrib import admin

# Register your models here.

from mypage.models import book_list, item_information

admin.site.register(item_information)
admin.site.register(book_list)
                                                                             
