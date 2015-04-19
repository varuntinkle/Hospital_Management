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
	url(r'^login/faq$',views.load_faq),
	url(r'^login/edit_profile$',views.edit_profile),
	url(r'^login/pat_prof_sub$',views.pat_prof_sub),
	url(r'^noticeboard/',include('blog.urls')),
	url(r'^login/new_notice$',views.new_notice),
	url(r'^login/adduser$',views.call_adduser),
	url(r'^login/notice_submit$',views.notice_submit),
	url(r'^login/user_added$',views.user_added),
	url(r'^login/stats$',views.call_stats),
	url(r'^login/med_forms$',views.med_forms),
	url(r'^login/viewdoctors$',views.admin_viewdoctor),


	#url(r'^login/recep_homepage$',views.recep_homepage),
	url(r'^$', views.index, name='index'),
    ]