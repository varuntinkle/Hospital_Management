from django.conf.urls import url
from . import views
from django.views.generic import TemplateView

urlpatterns = [
                url(r'^$', views.home_page, name='home_page'),
                url(r'^login/(?P<tag>\w+)$', views.login_page, name='login_page'),
                url(r'^$', views.login, name='reception'),
                url(r'^rec_form', views.rec_form , name='rec_form'),
                url(r'^redirect_home', views.redirect_home , name='redirect_home'),
                url(r'^reception', views.reception, name='reception'),
                url(r'^doctor_home', views.doctor_home, name='doctor_home'),
                url(r'^waiting_list',views.waiting_list,name='wl'),
                url(r'^completed_list',views.completed_list,name='cl'),
                url(r'^current_patient',views.current_patient,name='cp'),
                url(r'^patient_history',views.patient_history,name='ph'),
                url(r'^med_search1' , views.med_search1 , name='med_search1'),
                url(r'^doc_search' , views.doc_search , name='doc_search'),
                url(r'^rec_completed_list',views.rec_completed_list,name='rcl'),
                url(r'^rec_waiting_list',views.rec_waiting_list,name='rwl'),
                url(r'^rec_pending_list',views.rec_pending_list,name='rpl'),
                url(r'^print/(?P<tag>\w+)$',views.print_prescription,name='pp'),
                url(r'^logout$', views.logout_page, name='logout'),
                 
                url(r'^complaint/$',views.cmain , name='cmain'),
                url(r'^complaint/booking/$' , views.booking , name='booking'),                                        
                url(r'^complaint/booking/response/$' , views.response , name='response'),
                url(r'^complaint/cancel/',views.cancel,name='cancel'),
                url(r'^complaint/(?P<question_id>\d+)/cancelcomplaint/$', views.cancelcomplaint, name='cancelcomplaint'),
                url(r'^complaint/cancelconfirm/',views.cancelconfirm,name='cancelconfirm'),
                url(r'^complaint/adminmain/',views.adminmain , name='adminmain'),
                #(r'^complaint/(?P<question_id>\d+)/view/', views.viewcomplaint, name='viewcomplaint'),
                url(r'^complaint/viewcomplaintsave/' , views.viewcomplaintsave , name="viewcomplaintsave"),
                url(r'^complaint/med/' , views.med , name='med'),
                # url(r'^complaint/category/', views.category, name='category'),
                # url(r'^complaint/status/', views.status, name='status'),
                # url(r'^complaint/progress/',views.progress, name='progress'),

                 url(r'^f1/$', views.f1, name='f1'),
                url(r'^f1_detail/(?P<pk>[0-9]+)$', views.f1_detail),
                url(r'^reply/(?P<pk>[0-9]+)$', views.reply),
                url(r'^delete/$', views.delete, name='delete'),
                url(r'^followup/(?P<pres_id>\d+)', views.followup , name='followup'),
                 url(r'^followup/studfollowup/(?P<pres_id>\d+)', views.studfollowup , name='studfollowup'),
                 url(r'^followup/$', views.followup , name='followup'),
                 #######medicine
                url(r'^med/$' , views.med , name='med'),
                 url(r'^med/med_search/$' , views.med_search , name='med_search'),
                url(r'^med/dis_search/$' , views.dis_search , name='dis_search'),

                 #kenil
                url(r'^med_account$', views.med_account, name='rim_login'),
                url(r'^req_acc', views.req_acc , name='req_acc'),
                url(r'^in_rim', views.in_rim, name='in_rim'),
                url(r'^main', views.main, name='main'),
                url(r'^ins_scheme', views.ins_scheme, name='ins_scheme'),

                ]
