from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^login/authenticate$',views.authenticate),
	url(r'^login/logout$',views.logout),
<<<<<<< HEAD
	url(r'^login/appointment$',views.call_appoint),
=======
	url(r'^login/recep_homepage$',views.recep_homepage),
>>>>>>> 782264e2ee584a1c9a44c7538a63947de612cd80
    url(r'^$', views.index, name='index'),
    ]