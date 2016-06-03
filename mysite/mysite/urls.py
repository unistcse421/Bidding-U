from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView
import mysite.views
from django.contrib import admin


urlpatterns = [
	url(r"^$", TemplateView.as_view(template_name="homepage.html"), name="home"),
	url(r"^admin/", include(admin.site.urls)),
	url(r"^account/signup/$", mysite.views.SignupView.as_view(), name="account_signup"),
	url(r"^account/", include("account.urls")),
	url(r"^mypage/", include("mypage.urls")),
	url(r"^auction/", include("auction.urls")),
	url(r"^bidding/", include("bidding.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
