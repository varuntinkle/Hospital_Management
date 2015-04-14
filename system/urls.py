#####NIkit Prabodh########
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^graphindex$', views.graphindex, name='graphindex'),
    url(r'^graphdisease$', views.choosefunction, name='choosefunction'),
    url(r'^graphmedicine$', views.choosefunctionmed, name='choosefunctionmed'),
    url(r'^diseasewordcloud$', views.diseasewordcloud, name='diseasewordcloud'),
    url(r'^graphfollowup$', views.choosefunction_followup, name='choosefunction_followup'),
   # url(r'^ambulanceform$', views.ambulanceform, name='ambulanceform'),
 
    #####end NIkit Prabodh########
    
]