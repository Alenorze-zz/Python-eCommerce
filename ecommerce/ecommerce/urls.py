from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.contrib import admin

from .views import home_page, about_page, contact_page, login_page, register_page
from products.views import (
    ProductListView, 
    ProductDetailView, 
    ProductFeaturedListView, 
    ProductFeaturedDetailView
) 


urlpatterns = [
    url(r'^$', home_page),
    url(r'^about/$', about_page),
    url(r'^contact/$', contact_page),
    url(r'^login/$', login_page),
    url(r'^register/$', register_page),
    url(r'^products/$', ProductListView.as_view()),
    url(r'^products/(?P<pk>\d+)/$', ProductDetailView.as_view()),
    url(r'^admin/', admin.site.urls),
]


if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
