#from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from database.models import Registration, Patient, AmbulanceSchedule
import django.contrib.auth.hashers
from django.shortcuts import render 
# Create your views here.

def index(request):
    # Request the context of the request.
    # The context contains information such as the client's machine details, for example.
    context = RequestContext(request)
    if 'index' not  in request.session:
            return render_to_response('login/login.html', context)
    else:
        username =request.session["index"]
        Object_Searched = Registration.objects.filter(username = username)
        Object_Searched = Object_Searched[0]
        Category = Object_Searched.category
        
        if(Category==1):
            context_dict = {'object_reg': Object_Searched}
            return render(request,'login/doctor_homepage.html', context_dict)
        elif(Category==2):
            object_pat = Patient.objects.filter(username = username)
            object_pat = object_pat[0]
            context_dict = {'object_reg': Object_Searched,'object_pat': object_pat}
            return render(request,'login/patient.html', context_dict)
        elif(Category==3):
            Access_Schedule = AmbulanceSchedule.objects.all()
            context_dict = {'object_reg': Object_Searched, 'object_schedule': Access_Schedule}
            return render(request,'login/recep_homepage.html', context_dict)


def logout(request):
    if 'index'  in request.session:
         del request.session['index']    
    return HttpResponseRedirect("/")

def authenticate (request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        Object_Searched = Registration.objects.filter(username = username)
        if Object_Searched:
            Object_Searched = Object_Searched[0]
            if  password == Object_Searched.password:
                #django.contrib.auth.hashers.check_password(password, Object_Searched.password):
                Category=Object_Searched.category
                message=Object_Searched.id
                request.session["index"]=Object_Searched.username
                return HttpResponseRedirect("/")
            else:
                message = "Wrong Password"
                return HttpResponse(message)  
        else:
            message="Wrong Username"
            return HttpResponse(message)


def call_appoint(request):
    context = RequestContext(request)
    if 'index' not  in request.session:
        return render_to_response('login/login.html', context)
    else:
        return render_to_response('login/appointment.html', context)

def recep_homepage (request):
    if request.method == 'POST':
        day = request.POST['Day']
        timeh = request.POST['Time_h']
        timem = request.POST['Time_m']
        time = timeh+":"+timem+":00"
        
        availability1 = request.POST['availability']
        if(availability1=='0'):
            available=False
        else:
            available=True
        Schedule_Search = AmbulanceSchedule.objects.filter(Day = day, Time = time)
        
        if Schedule_Search:
            Schedule_Search = Schedule_Search[0]
            Schedule_Search.Availability = available
            Schedule_Search.save()

        else:
            new_schedule = AmbulanceSchedule(Day=day,Time=time,Availability=available,Count=0)
            new_schedule.save()
        return HttpResponseRedirect("/")


