from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^login/authenticate$',views.authenticate),
	url(r'^login/logout$',views.logout),
	url(r'^login/appointment$',views.call_appoint),
	url(r'^login/ambulance$',views.book_amb),
	url(r'^login/amb_submit$',views.set_amb_sch),
	url(r'^login/recep_homepage$',views.recep_homepage),
	url(r'^$', views.index, name='index'),
    ]