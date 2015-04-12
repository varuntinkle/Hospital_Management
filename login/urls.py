from django.conf.urls import include, url

from . import views

urlpatterns = [
	url(r'^login/authenticate$',views.authenticate),
	url(r'^login/logout$',views.logout),
	url(r'^login/appointment$',views.call_appoint),
	url(r'^login/recep_schedule$',views.call_recep_schedule),
	url(r'^login/ambulance$',views.book_amb),
	url(r'^login/recep_submit$',views.end_recep_schedule),
	url(r'^login/amb_submit$',views.set_amb_sch),
	url(r'^noticeboard$',include('blog.urls')),
	#url(r'^login/recep_homepage$',views.recep_homepage),
	url(r'^$', views.index, name='index'),
    ]