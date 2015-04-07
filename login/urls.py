from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^login/authenticate',views.authenticate),
<<<<<<< HEAD
	url(r'^login/logout',views.logout),
=======
	url(r'^logout',views.logout),
>>>>>>> 68f0e24ea15b4068fd73b88fd0bdc26929927a58
    url(r'', views.index, name='index'),
    ]