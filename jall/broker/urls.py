from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView, DetailsView, RedeemView, BalanceView, HeartbeatView

urlpatterns = [
    url(r'^tokens/$', CreateView.as_view(), name="create"),
    url(r'^tokens/(?P<pk>[0-9]+)/$',
        DetailsView.as_view(), name="details"),
    url(r'^tokens/redeem/(?P<pk>[0-9]+)/$',
        RedeemView.as_view(), name="redeem"),
    url(r'^balance/', BalanceView.as_view(), name='balance'),
    url(r'^heartbeat/', HeartbeatView.as_view(), name='heartbeat')
]
urlpatterns = format_suffix_patterns(urlpatterns)