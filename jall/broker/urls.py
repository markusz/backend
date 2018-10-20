from django.urls import path
from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView, DetailsView

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^tokens/$', CreateView.as_view(), name="create"),
    url(r'^tokens/(?P<pk>[0-9]+)/$',
        DetailsView.as_view(), name="details"),
]
urlpatterns = format_suffix_patterns(urlpatterns)