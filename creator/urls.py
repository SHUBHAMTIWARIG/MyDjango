from django.conf.urls import url

from creator.views import creator_view, creator_add, creator_detail

urlpatterns = [
    url(r'^creator/', creator_view, "list"),
    url(r'^creator/(?P<id>\d+)/$', creator_detail, name='detail'),
    url(r'^creator/add/', creator_add, "add"),
]
