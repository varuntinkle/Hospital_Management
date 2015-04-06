from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^login/authenticate',views.authenticate),
    url(r'', views.index, name='index'),
    ]