#from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from database.models import CRequest, Prescription, Reception, Registration, Patient, AmbulanceSchedule, AmbulanceBooking, Post, Doctor
import django.contrib.auth.hashers
from django.shortcuts import render
from django.contrib import messages
import datetime
import time
#from datetime import datetime
# Create your views here.

def index(request):
    # Request the context of the request.
    # The context contains information such as the client's machine details, for example.
    context = RequestContext(request)
    if 'index' not  in request.session:
            return render(request,'login/login.html', {})
    else:
        username =request.session["index"]
        Object_Searched = Registration.objects.filter(username = username)
        Object_Searched = Object_Searched[0]
        Category = Object_Searched.category
        
        if(Category==1):
            object_notice = Post.objects.all().order_by('-date')[:5]
            context_dict = {'object_reg': Object_Searched, 'object_notice':object_notice}
            return render(request,'login/doctor_homepage.html', context_dict)
        elif(Category==2):
            object_pat = Patient.objects.filter(username = username)
            object_pat = object_pat[0]
            object_pres = Prescription.objects.filter(reg_no = object_pat)
            object_notice = Post.objects.all().order_by('-date')[:5]
            for pres in object_pres:
                temp = pres.medicine.replace('u\'',' ').replace('[',' ').replace(']',' ').replace('\'',' ')
                pres.medicine = temp
                pres.save()
            context_dict = {'object_pres':object_pres,'object_reg': Object_Searched,'object_pat': object_pat, 'object_notice':object_notice}
            return render(request,'login/patient_homepage.html', context_dict)
        elif(Category==3):
            Access_Schedule = AmbulanceSchedule.objects.all()
            object_notice = Post.objects.all().order_by('-date')[:5]
            context_dict = {'object_reg': Object_Searched, 'object_schedule': Access_Schedule, 'object_notice':object_notice}
            return render(request,'login/recep_homepage.html', context_dict)
        elif(Category==4):
            object_notice = Post.objects.all().order_by('-date')[:5]
            context_dict = {'object_reg': Object_Searched, 'object_notice':object_notice}
            return render(request,'login/admin_homepage.html',context_dict)


def logout(request):
    if 'index'  in request.session:
         del request.session['index']    
    return HttpResponseRedirect("/")

def authenticate (request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        #password = django.contrib.auth.hashers.make_password(password, salt=None, hasher='default')
        Object_Searched = Registration.objects.filter(username = username)
        if Object_Searched:
            Object_Searched = Object_Searched[0]
            if  django.contrib.auth.hashers.check_password(password, Object_Searched.password) or password==Object_Searched.password:
                #django.contrib.auth.hashers.check_password(password, Object_Searched.password):
                Category=Object_Searched.category
                message=Object_Searched.id
                request.session["index"]=Object_Searched.username
                return HttpResponseRedirect("/")
            else:

                message = "Wrong Password"
                messages.error(request, message)
                return HttpResponseRedirect("/#about")  
        else:
            message="Wrong Username"
            messages.error(request, message)
            return HttpResponseRedirect("/#about")


def call_appoint(request):
    context = RequestContext(request)
    if 'index' not  in request.session:
        return HttpResponseRedirect("/")
    else:    
        Object_Searched = Registration.objects.filter(username = request.session["index"])
        Object_Searched = Object_Searched[0]
        if Object_Searched.category==2:
            object_doc = Doctor.objects.all()
            context_dict = {'object_doc': object_doc}
            return render(request,'login/appointment.html',context_dict)
        else:
            return render_to_response('login/permission_error.html')


def book_amb(request):
    context = RequestContext(request)
    if 'index' not  in request.session:
        return HttpResponseRedirect("/")
    else:    
        Object_Searched = Registration.objects.filter(username = request.session["index"])
        Object_Searched = Object_Searched[0]
        if Object_Searched.category==2:
            Object_Searched = AmbulanceSchedule.objects.all()
            context_dict = {'object_amb': Object_Searched}
            return render(request,'login/ambulance.html', context_dict)
        else:
            return render_to_response('login/permission_error.html')

def edit_profile(request):
    context = RequestContext(request)
    if 'index' not  in request.session:
        return HttpResponseRedirect("/")
    else:    
        Object_Searched = Registration.objects.filter(username = request.session["index"])
        Object_Searched = Object_Searched[0]
        if Object_Searched.category==2:
            object_pat = Patient.objects.filter(username = request.session["index"])
            object_pat = object_pat[0]
            return render(request,'login/patient_profile.html', {'object_pat':object_pat})
        else:
            return render_to_response('login/permission_error.html')

def load_faq(request):
    context = RequestContext(request)
    if 'index' not  in request.session:
        return HttpResponseRedirect("/")
    else:    
        Object_Searched = Registration.objects.filter(username = request.session["index"])
        Object_Searched = Object_Searched[0]
        if Object_Searched.category==2:
            return render(request,'login/faq.html', {})
        else:
            return render_to_response('login/permission_error.html')

def med_forms(request):
    context = RequestContext(request)
    if 'index' not  in request.session:
        return HttpResponseRedirect("/")
    else:    
        Object_Searched = Registration.objects.filter(username = request.session["index"])
        Object_Searched = Object_Searched[0]
        if Object_Searched.category==2:
            return render(request,'login/med_forms.html', {})
        else:
            return render_to_response('login/permission_error.html')
               
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

def fix_appoint(request):
    if request.method=="POST":
        problem=request.POST['problem']

        doctor=Doctor.objects.get(name=request.POST['doctor_list'])
        time=request.POST['time'].split()
        time=time[0]+":00"
        datetimedd=request.POST['date']+" "+time
        Object_Searched = Patient.objects.get(username = request.session["index"])
        list=CRequest.objects.all()
        appoint_no=1
        new_object=CRequest(name=Object_Searched.name,reg_no=Object_Searched,problem=problem,request_date=datetime.datetime.now(),appoint_date=datetimedd,appoint_no=appoint_no,doctor=doctor,status=0)
        new_object.save()
    return HttpResponseRedirect("/")

def pat_prof_sub(request):
    if request.method=="POST":
        name=request.POST['name']
        age=request.POST['age']
        height=request.POST['height']
        weight=request.POST['weight']
        new_patient=Patient.objects.filter(username = request.session["index"])
        new_patient=new_patient[0]
        new_patient.name=name
        new_patient.age=age
        new_patient.height=height
        new_patient.weight=weight
        new_patient.save()
        Object_Searched = Registration.objects.filter(username = request.session["index"])
        Object_Searched = Object_Searched[0]
        Object_Searched.name=name
    return HttpResponseRedirect("/")        
    
def call_recep_schedule(request):
    context = RequestContext(request)
    if 'index' not  in request.session:
        return HttpResponseRedirect("/")
    else:    
        Object_Searched = Registration.objects.filter(username = request.session["index"])
        Object_Searched = Object_Searched[0]
        if Object_Searched.category==3:
            Access_Schedule = AmbulanceSchedule.objects.all().order_by('-Day').reverse()
            context_dict = {'object_schedule': Access_Schedule}
            return render(request,'login/recep_schedule.html', context_dict)
        else:
            return render_to_response('login/permission_error.html')

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
    return HttpResponseRedirect("/")

def new_notice(request):
    context = RequestContext(request)
    if 'index' not  in request.session:
        return HttpResponseRedirect("/")
    else:    
        Object_Searched = Registration.objects.filter(username = request.session["index"])
        Object_Searched = Object_Searched[0]
        if Object_Searched.category==3:
            Access_Post = Post.objects.all()
            context_dict = {'object_schedule': Access_Post}
            return render(request,'login/new_notice.html', context_dict)
        else:
            return render_to_response('login/permission_error.html')
    
'''def call_adduser(request):
    context = RequestContext(request)
    if 'index' not  in request.session:
        return HttpResponseRedirect("/")
    else:    
        Object_Searched = Registration.objects.filter(username = request.session["index"])
        Object_Searched = Object_Searched[0]
        if Object_Searched.category==4:
            context_dict = {}
            return render(request,'login/admin_adduser.html', context_dict)
        else:
            return render_to_response('login/permission_error.html')

'''

def call_adddoctor(request):
    context = RequestContext(request)
    if 'index' not  in request.session:
        return HttpResponseRedirect("/")
    else:    
        Object_Searched = Registration.objects.filter(username = request.session["index"])
        Object_Searched = Object_Searched[0]
        if Object_Searched.category==4:
            context_dict = {}
            return render(request,'login/admin_adddoctor.html', context_dict)
        else:
            return render_to_response('login/permission_error.html')   


def call_addreception(request):
    context = RequestContext(request)
    if 'index' not  in request.session:
        return HttpResponseRedirect("/")
    else:    
        Object_Searched = Registration.objects.filter(username = request.session["index"])
        Object_Searched = Object_Searched[0]
        if Object_Searched.category==4:
            context_dict = {}
            return render(request,'login/admin_addreception.html', context_dict)
        else:
            return render_to_response('login/permission_error.html')   


def call_addadmin(request):
    context = RequestContext(request)
    if 'index' not  in request.session:
        return HttpResponseRedirect("/")
    else:    
        Object_Searched = Registration.objects.filter(username = request.session["index"])
        Object_Searched = Object_Searched[0]
        if Object_Searched.category==4:
            context_dict = {}
            return render(request,'login/admin_addadmin.html', context_dict)
        else:
            return render_to_response('login/permission_error.html')   

def notice_submit(request):
    if request.method == 'POST':
        title=request.POST['title']
        body=request.POST['body']
        date=datetime.now()

        new_notice = Post(title=title,body=body,date=date)
        new_notice.save()
        return HttpResponseRedirect("/")
    #return HttpResponseRedirect("/")

def user_added(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        password=django.contrib.auth.hashers.make_password(password, salt=None, hasher='default')
        name=request.POST['name']
        category=request.POST['category']
        new_user = Registration(username=username,password=password,name=name,category=category)
        new_user.save()
        if(category=='1'):
            new_doc = Doctor(username=username,name=name,speciality="NA",qualification="NA",patients_visited="NA",schedule="NA")
            new_doc.save()
        elif(category=='2'):
            new_patient = Patient(username=username,reg_no="X",name=name,age=0,height="",weight=0,patient_history="NA",patient_test="NA")
            new_patient.save()
        elif(category=='3'):
            new_recep=Reception(username=username)
            new_recep.save()
        return HttpResponseRedirect("/")


def doctor_added(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        speciality=request.POST['speciality']
        qualification=request.POST['qualification']
        password=django.contrib.auth.hashers.make_password(password, salt=None, hasher='default')
        name=request.POST['name']
        category=1
        new_user = Registration(username=username,password=password,name=name,category=category)
        new_user.save()
        new_doc = Doctor(name=name,speciality=speciality,qualification=qualification,patients_visited="NA",schedule="NA")
        new_doc.save()
        return HttpResponseRedirect("/")

def admin_added(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        password=django.contrib.auth.hashers.make_password(password, salt=None, hasher='default')
        name=request.POST['name']
        category=4
        new_user = Registration(username=username,password=password,name=name,category=category)
        new_user.save()
        return HttpResponseRedirect("/")


def reception_added(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        password=django.contrib.auth.hashers.make_password(password, salt=None, hasher='default')
        name=request.POST['name']
        category=3
        new_user = Registration(username=username,password=password,name=name,category=category)
        new_user.save()
        return HttpResponseRedirect("/")



def call_stats(request):
    context = RequestContext(request)
    if 'index' not  in request.session:
        return HttpResponseRedirect("/")
    else:  
        request.session["fav_color"] = "blue"  
        Object_Searched = Registration.objects.filter(username = request.session["index"])
        Object_Searched = Object_Searched[0]
        if Object_Searched.category==1 or Object_Searched.category==4:
            return render_to_response('system/graphindex.html', context)
        else:
            return render_to_response('login/permission_error.html')


def admin_viewdoctor(request):

    Objects = Doctor.objects.all()
    c1=0
    context_dict={}
    for x in Objects:
         x1=[]
         x1.append(x.name)
         x1.append(x.speciality)
         x1.append(x.qualification)
         x1.append(x.patients_visited)
         x1.append(x.schedule)
         context_dict[str(c1)]=x1
         c1+=1
    return render(request,'login/admin_viewdoctors.html',context_dict)

def call_doctor_schedule(request):
    context = RequestContext(request)
    if 'index' not  in request.session:
        return HttpResponseRedirect("/")
    else:    
        Object_Searched = Registration.objects.filter(username = request.session["index"])
        Object_Searched = Object_Searched[0]
        if Object_Searched.category==3:
            Access_Doctor = Doctor.objects.all().order_by('-name').reverse()
            context_dict = {'object_doctor': Access_Doctor}
            return render(request,'login/doctor_schedule.html', context_dict)
        else:
            return render_to_response('login/permission_error.html')

def end_doctor_schedule(request):
    if request.method == 'POST':
        username = request.POST['doctor_name']
        sch = request.POST['sch_details']
        doctor_search = Doctor.objects.filter(username = username)
        if doctor_search:
                doctor_search = doctor_search[0]
                doctor_search.schedule = sch
                doctor_search.save()

    return HttpResponseRedirect("/")

def call_addpatient(request):
    context = RequestContext(request)
    if 'index' not  in request.session:
        return HttpResponseRedirect("/")
    else:    
        Object_Searched = Registration.objects.filter(username = request.session["index"])
        Object_Searched = Object_Searched[0]
        if Object_Searched.category==3:
            context_dict = {}
            return render(request,'login/recep_addpatient.html', context_dict)
        else:
            return render_to_response('login/permission_error.html') 

def end_addpatient(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        name=request.POST['name']
        category='2'
        reg=request.POST['reg']
        new_user = Registration(username=username,password=password,name=name,category=category)
        new_user.save()
        new_patient = Patient(username=username,reg_no="reg",name=name,age=0,height="",weight=0,patient_history="NA",patient_test="NA")
        new_patient.save()
        return HttpResponseRedirect("/")

#    Objects = Doctor.objects.all()
#    c1=0
#    context_dict={}
#    list1=[]
#    for x in Objects:
#        list1.append(x.name)
#   list1.append(x.speciality)
#   list1.append(x.qualification)
#   list1.append(x.schedule)
#    context_dict['links']=list1
    return render_to_response('login/admin_viewdoctors.html', {'obj': Doctor.objects.all()})


def admin_viewpatient(request):
#    Objects = Doctor.objects.all()
#    c1=0
#    context_dict={}
#    list1=[]
#    for x in Objects:
#        list1.append(x.name)
#   list1.append(x.speciality)
#   list1.append(x.qualification)
#   list1.append(x.schedule)
#    context_dict['links']=list1
    return render_to_response('login/admin_viewpatients.html', {'objs': Patient.objects.all()})

