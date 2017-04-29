from django.conf.urls import url

from polls.views import home

urlpatterns = [url(r'^$', home,name="base")
               ]
