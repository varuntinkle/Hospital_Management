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

	url(r'^noticeboard/',include('blog.urls')),
	url(r'^login/new_notice$',views.new_notice),
	#url(r'^login/adduser$',views.call_adduser),
	url(r'^login/adddoctor$',views.call_adddoctor),
	url(r'^login/addreception$',views.call_addreception),
	url(r'^login/addadmin$',views.call_addadmin),
	url(r'^login/notice_submit$',views.notice_submit),
	url(r'^login/user_added$',views.user_added),
	url(r'^login/doctor_added$',views.doctor_added),
	url(r'^login/admin_added$',views.admin_added),
	url(r'^login/reception_added$',views.reception_added),
	url(r'^login/stats$',views.call_stats),
	url(r'^login/viewdoctors$',views.admin_viewdoctor),


	#url(r'^login/recep_homepage$',views.recep_homepage),
	url(r'^$', views.index, name='index'),
    ]