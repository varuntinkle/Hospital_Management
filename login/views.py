#from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from database.models import Registration, Patient, AmbulanceSchedule, AmbulanceBooking, Post
import django.contrib.auth.hashers
from django.shortcuts import render
import datetime
from datetime import datetime
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
            object_notice = Post.objects.all().order_by('-date')[:5]
            context_dict = {'object_reg': Object_Searched,'object_pat': object_pat, 'object_notice':object_notice}
            return render(request,'login/patient.html', context_dict)
        elif(Category==3):
            Access_Schedule = AmbulanceSchedule.objects.all()
            object_notice = Post.objects.all().order_by('-date')[:5]
            context_dict = {'object_reg': Object_Searched, 'object_schedule': Access_Schedule, 'object_notice':object_notice}
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
        return HttpResponseRedirect("/")
    else:
        return render_to_response('login/appointment.html', context)


def book_amb(request):
    context = RequestContext(request)
    if 'index' not  in request.session:
        return HttpResponseRedirect("/")
    else:
        Object_Searched = AmbulanceSchedule.objects.all()
        context_dict = {'object_amb': Object_Searched}
        return render(request,'login/ambulance.html', context_dict)
               
def set_amb_sch(request):
    if request.method=="POST":
        source=request.POST['source']
        destination=request.POST['destination']
        day_time=request.POST['DayTime']
        purpose=request.POST['purpose']
        present_date=datetime.datetime.now()
        listed=day_time.split(",")
        day=listed[0]
        time=listed[1]
        time_list=time.split(" ")
        if (time_list[1]=="a.m."):
            time=time_list[0]+":00"
        else:
            lst=time_list[0].split(":")
            hours=str(int(lst[0])+12)
            mins=lst[1]
            time=hours+":"+mins+":00"
        new_object=AmbulanceBooking(Source=source,Destination=destination,DateBooked=present_date,Purpose=purpose,Day=day,Time=time)
        new_object.save()
        search = AmbulanceSchedule.objects.filter(Day = day, Time = time)
        if search:
            search=search[0]
            search.Count=search.Count+1
            search.save()
    return HttpResponseRedirect("/")
    
def call_recep_schedule(request):
    context = RequestContext(request)
    if 'index' not  in request.session:
        return HttpResponseRedirect("/")
    else:
        Access_Schedule = AmbulanceSchedule.objects.all().order_by('-Day').reverse()
        context_dict = {'object_schedule': Access_Schedule}
        return render(request,'login/recep_schedule.html', context_dict)

def end_recep_schedule(request):
    if request.method == 'POST':

        if 'commit' in request.POST:
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
        elif 'reset' in request.POST:
            reset_day = request.POST['reset_day']
            AmbulanceSchedule.objects.filter(Day = reset_day).delete()
            AmbulanceBooking.objects.filter(Day = reset_day).delete()
            return HttpResponseRedirect("/")
    #return HttpResponseRedirect("/")

def new_notice(request):
    context = RequestContext(request)
    if 'index' not  in request.session:
        return HttpResponseRedirect("/")
    else:
        Access_Post = Post.objects.all()
        context_dict = {'object_schedule': Access_Post}
        return render(request,'login/new_notice.html', context_dict)

def notice_submit(request):
    if request.method == 'POST':
        title=request.POST['title']
        body=request.POST['body']
        date=datetime.now()

        new_notice = Post(title=title,body=body,date=date)
        new_notice.save()
        return HttpResponseRedirect("/")
    #return HttpResponseRedirect("/")
