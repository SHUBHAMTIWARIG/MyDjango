from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from accounts.views import (login_view, logout_view, register_view)
from creator.views import creator_view

urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^login/', login_view, name="login"),
    url(r'^logout/', logout_view, name="logout"),
    url(r'^register/', register_view, name="register"),
    url(r'',include('giveaways.urls')),
    url(r'',include('creator.urls')),
    url(r'', include('polls.urls')),

]  # allow apps to upload files to server
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
