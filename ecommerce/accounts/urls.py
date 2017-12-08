from django.conf.urls import url

from .views import (
    AccountsHomeView,
)


urlpatterns = [
    url(r'^$', AccountsHomeView.as_view(), name='home'),
]
