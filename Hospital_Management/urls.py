from django.conf.urls import include, url
from django.contrib import admin
urlpatterns = [
    # Examples:
    # url(r'^$', 'testing2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
     url(r'^noticeboard/', include('blog.urls')),
     url(r'^system/', include('system.urls')),
    url(r'^', include('login.urls') ),
  	url(r'^rtc/', include('rtc.urls')),
]