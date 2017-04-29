from django.conf.urls import url

from giveaways.views import giveaways_view, giveaway_detail, giveaway_add,giveaway_delete

urlpatterns = [
    url(r'^give/', giveaways_view,"list"),
    url(r'^give/(?P<id>\d+)/$', giveaway_detail, name='detail'),
    url(r'^give/(?P<id>\d+)/delete/$', giveaway_delete, name='delete'),
    url(r'^give/add/', giveaway_add,"add"),
]