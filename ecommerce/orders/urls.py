from django.conf.urls import url

from .views import (
    OrderListView,
    OrderDetailView
)


urlpatterns = [
    url(r'^$', OrderDetailView.as_view(), name='list'),
    url(r'^(?P<order_id>[0-9A-Za-z]+)/$', OrderDetailView.as_view(), name='detail'),
]
