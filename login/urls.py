from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^login/authenticate$',views.authenticate),
	url(r'^login/logout$',views.logout),
	url(r'^login/appointment$',views.call_appoint),
	url(r'^login/recep_homepage$',views.recep_homepage),
    url(r'^$', views.index, name='index'),
    ]