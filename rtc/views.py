from rtc.managedatabase import getprescriptiondetails,getprescriptionspecific
from datetime import timedelta
from django.shortcuts import render,render_to_response,redirect
from django.http import HttpResponse
from django.template import RequestContext, loader
from database.models import CRequest,Medicine,FollowUp,Complaint,Doctor,Prescription,Reception,Patient,Internal_rim,Finance_accountant
import datetime
from datetime import date
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q	
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.contrib import messages

page_typ = 1

def home_page(request):
	return render(request,'home.html')

def login_page(request,tag):
	global page_typ
	if tag != "login":
		page_typ = tag
	if request.method == 'GET':
		return render(request,'login.html' )
	elif request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				return redirect('/rtc/redirect_home')
		else:
			return render(request, 'error.html', {"error_message": 'Atleast one of the given username and password is incorrect.'})

@login_required
def redirect_home(request):
	global page_typ
	username = str(request.user)
	if len(Patient.objects.filter(username = username)) > 0:
		if page_typ == '2':
			return redirect('/rtc/complaint/')
		elif page_typ == '3':
			return redirect('/rtc/followup/')
		elif page_typ == '5':
			return redirect('/rtc/main/')
		else :
			return render(request, 'error.html', {"error_message": "Patient cannot access this page!"})
	elif len(Doctor.objects.filter(username = username)):
		if page_typ == '1':
			return redirect('/rtc/doctor_home/')
		elif page_typ == '3':
			return redirect('/rtc/f1/')
		else :
			return render(request, 'error.html', {"error_message": "Doctor cannot access this page!"})
	elif len(Reception.objects.filter(username = username)):
		if page_typ == '1':
			return redirect('/rtc/reception/')
		else :
			return render(request, 'error.html', {"error_message": "Reception cannot access this page!"})
	elif len(Finance_accountant.objects.filter(username = username)):
		if page_typ == '5':
			return redirect('/rtc/med_account')
		if page_typ == '2':
			return redirect('/rtc/complaint/adminmain/')
	else:
		return render(request, 'error.html', {"error_message": "User does not exist in RTC!"})


######################################################################################
########################################Complaint##################################
######################################################################################
@login_required
def cmain(request):
	username = request.user.username
	if len(Patient.objects.filter(username = username)) == 0:
		return render(request, 'error.html', {"error_message": "Only a Patient can access this page!"})
	else:
	    username = request.user.username
	    latest_complaints = Complaint.objects.all().filter(username=username)
	    com=Complaint.objects.all().filter(username=username)

	    template = loader.get_template('complaintbooking/main.html')
	    context = RequestContext(request,{'latest_complaint': latest_complaints,'cn':len(com)})
	    return HttpResponse(template.render(context))

@login_required
def booking(request):
	username = request.user.username
	if len(Patient.objects.filter(username = username)) == 0:
		return render(request, 'error.html', {"error_message": "Only a Patient can access this page!"})
	else:
	    username = request.user.username
	    com=Complaint.objects.all().filter(username=username)
	    template = loader.get_template('complaintbooking/book.html')
	    context = RequestContext(request,{'cn':len(com)})
	    return HttpResponse(template.render(context))

@login_required
def response(request):
	username = request.user.username
	if len(Patient.objects.filter(username = username)) == 0:
		return render(request, 'error.html', {"error_message": "Only a Patient can access this page!"})
	else:
		if request.method =='POST':
			category = request.POST['category']
			subject = request.POST['subject']
			description = request.POST['description']        
			b = Complaint(username=username , category=category , subject=subject , complaint=description , complaint_date = timezone.now(),process='not_seen')
			b.save() 
			return HttpResponseRedirect('/rtc/complaint/')     

@login_required
def cancel(request):
	username = request.user.username
	if len(Patient.objects.filter(username = username)) == 0:
		return render(request, 'error.html', {"error_message": "Only a Patient can access this page!"})
	else:
	    username = request.user.username
	    com=Complaint.objects.all().filter(username=username)
	    latest_complaints = Complaint.objects.all().filter(username=username,process='not_seen')
	    template = loader.get_template('complaintbooking/cancel.html')
	    context = RequestContext(request,{'latest_complaint': latest_complaints,'cn':len(com)})
	    return HttpResponse(template.render(context))

@login_required
def cancelcomplaint(request,question_id):
	username = request.user.username
	if len(Patient.objects.filter(username = username)) == 0:
		return render(request, 'error.html', {"error_message": "Only a Patient can access this page!"})
	else:
	    username = request.user.username
	    c=Complaint.objects.all().filter(pk=question_id)
	    c.delete()
	    return HttpResponseRedirect('/rtc/complaint/cancelconfirm')

@login_required
def cancelconfirm(request):
	username = request.user.username
	if len(Patient.objects.filter(username = username)) == 0:
		return render(request, 'error.html', {"error_message": "Only a Patient can access this page!"})
	else:
	    username = request.user.username
	    com=Complaint.objects.all().filter(username=username)
	    template = loader.get_template('complaintbooking/cancelconfirm.html')
	    context = RequestContext(request,{'cn':len(com)})
	    return HttpResponse(template.render(context))

@login_required
def adminmain(request):
	username = request.user.username
	if len(Finance_accountant.objects.filter(username = username)) == 0:
		return render(request, 'error.html', {"error_message": "Only a Admin can access this page!"})
	else:
	    complaints = Complaint.objects.all()
	    c=Complaint.objects.all().filter(process='not_seen')
	    template = loader.get_template('complaintbooking/admin_main.html')
	    context = RequestContext(request,{'complaint': complaints,'cn':len(c)})
	    return HttpResponse(template.render(context))

# def viewcomplaint(request,question_id):
#     c=Complaint.objects.all().filter(pk=question_id)
#     c1=Complaint.objects.all().filter(process='not_seen')
#     template = loader.get_template('complaintbooking/viewcomplaint.html')
#     context = RequestContext(request,{'complaint': c,'cn':len(c1)})
#     return HttpResponse(template.render(context))
@login_required
def viewcomplaintsave(request):
	username = request.user.username
	if len(Finance_accountant.objects.filter(username = username)) == 0:
		return render(request, 'errror.html', {"error_message": "Only a Admin can access this page!"})
	else:
	    if request.method =='POST':
	        process = request.POST['process']
	        question_id = request.POST['id_forsave']
	        admintext = request.POST['remarks']
	        c1 =Complaint.objects.all().filter(process='not_seen')
	        c = Complaint.objects.get(pk=question_id)
	        c.process = process
	        c.admintext = admintext
	        c.save()
	        return HttpResponseRedirect('/rtc/complaint/adminmain/')

###########################################################################
###########################################################################
###########################################################################



# def  category(request):
#     complaints = Complaint.objects.all()
#     c=Complaint.objects.all().filter(process='not_seen')
#     template = loader.get_template('complaintbooking/admin_category.html')
#     context = RequestContext(request,{'complaint': complaints,'cn':len(c)})
#     return HttpResponse(template.render(context))

# def status(request):
#     complaints = Complaint.objects.all()
#     c=Complaint.objects.all().filter(process='not_seen')
#     template = loader.get_template('complaintbooking/admin_status.html')
#     context = RequestContext(request,{'complaint': complaints,'cn':len(c)})
#     return HttpResponse(template.render(context))

# def progress(request):
#     complaints = Complaint.objects.all()
#     c=Complaint.objects.all().filter(process='not_seen')
#     template = loader.get_template('complaintbooking/progress.html')
#     context = RequestContext(request,{'complaint': complaints,'cn':len(c)})
#     return HttpResponse(template.render(context))

@login_required    
@csrf_exempt
def med_search1(request):
	if request.method=='POST':
		search_text=request.POST['value']
		res=Medicine.objects.all().filter(Q(name__contains=search_text) | Q(salt__contains=search_text))
		context={'res':res}
		return render(request,'med/med_search1.html',context)
	else:
          search_text='a'
          res=''
          
          res=Medicine.objects.all().filter(Q(name__contains=search_text) | Q(salt__contains=search_text))
          context = {'res' : res}
          return render(request,'med/med_search1.html',context)
          
@login_required    
@csrf_exempt
def doc_search(request):
	if request.method=='POST':
		search_text=request.POST['value']
		res=Doctor.objects.all().filter(Q(name__contains=search_text))
		context={'res':res}
		return render(request,'doc_search.html',context)
	else:
          search_text=''
          res=''
          res=Doctor.objects.all().filter(Q(name__contains=search_text))
          context = {'res' : res}
          return render(request,'doc_search.html',context)



def logout_page(request):
	logout(request)
	return redirect('/rtc/')



@login_required
def reception(request):
	username = request.user.username
	if len(Reception.objects.filter(username = username)) == 0:
		return render(request, 'error.html', {"error_message": "This page can only be accessed from the reception"})
	else:
		if request.method == 'GET':
			now = datetime.datetime.now()
			waiting =  CRequest.objects.filter(status= '0',appoint_date__year=now.year,appoint_date__month=now.month,appoint_date__day=now.day)
			pending =  CRequest.objects.filter(status= '1',appoint_date__year=now.year,appoint_date__month=now.month,appoint_date__day=now.day)
			completed =  CRequest.objects.filter(status= '2' , done = False,appoint_date__year=now.year,appoint_date__month=now.month,appoint_date__day=now.day)
			return render(request,'reception.html',{'waiting':waiting,'pending':pending,'completed':completed,'user':username})
		

@login_required
def rec_form(request):
    if request.method == 'GET':
        context={}
        return render(request,'rec_form.html')
    elif request.method == 'POST':
        name1 = request.POST['name']
        outsider1 = "outsider" in request.POST
        reg_number = request.POST['reg_no']
        if outsider1 == False:
        	try: reg_no1 = Patient.objects.get(reg_no=reg_number)
        	except: return render(request,'rec_form.html',{'error_message':"Either Patient is not registered or registration number entered is wrong"})
        problem1= request.POST['problem']
        submit_date1= datetime.datetime.now()
        appoint_date1 = datetime.datetime.now()
        appoint_no1 = request.POST['appoint_no']
        doc_name = request.POST['doctor']
        try: doctor1=Doctor.objects.get(name=doc_name)
        except: return render(request,'rec_form.html',{'error_message':"Doctor not Found"})
        done1=False
        #outsider1=False
        #status1 =  request.POST['status']
        if outsider1 == False:
        	b=CRequest(name=name1,reg_no=reg_no1,problem=problem1,request_date= submit_date1,appoint_date=appoint_date1,appoint_no=appoint_no1,doctor=doctor1,done=done1,outsider=outsider1,status='0')
        else:
      		b=CRequest(name=name1,problem=problem1,request_date= submit_date1,appoint_date=appoint_date1,appoint_no=appoint_no1,doctor=doctor1,done=done1,outsider=outsider1,status='0')  	
        b.save()
        return redirect('/rtc/reception')

@login_required
def doctor_home(request):
	username = request.user.username
	if len(Doctor.objects.filter(username = username)) == 0:
		return render(request, 'error.html', {"error_message": "Only a doctor can access this page!"})
	else:
		if(request.method == 'GET'):
			now = datetime.datetime.now()
			waiting_list= CRequest.objects.filter(doctor__username = username, status='0',appoint_date__year=now.year,appoint_date__month=now.month,appoint_date__day=now.day ).order_by('appoint_date').reverse()
			completed_list= CRequest.objects.filter(doctor__username = username, status='2',appoint_date__year=now.year,appoint_date__month=now.month,appoint_date__day=now.day ).order_by('appoint_date')
			Prescription_list = Prescription.objects.filter(doctor__username = username).order_by('prescription_time')
			pending = CRequest.objects.filter(doctor__username = username, status='1' ).order_by('appoint_date')
			date2 = date.today()
			date1 = date2 - timedelta(1)
			yest_min = datetime.datetime.combine(date1,datetime.time.min)
			yest_max = datetime.datetime.combine(date1,datetime.time.max)
			yest_list = Prescription.objects.filter(doctor__username = username, prescription_time__range=(yest_min,yest_max))
			date1 = date2-timedelta(7)
			week_list = Prescription.objects.filter(doctor__username = username, prescription_time__range= [date1,date2])
			date1 = date2 - timedelta(30)
			month_list = Prescription.objects.filter(doctor__username = username, prescription_time__range= [date1,date2])
			if not pending:  #######check this later
				if waiting_list:
					curpat = waiting_list[0]
					curpat.status = '1'
					curpat.save()
				else:
					curpat = []
			else:
				curpat  = pending[0]
			if curpat:
				history = Prescription.objects.filter(reg_no__reg_no=curpat.reg_no.reg_no)

			else:
				history = []
			waiting_list= CRequest.objects.filter(doctor__username = username, status='0' ).order_by('appoint_date').reverse()
			# assert(False)
			j=0;
			context = {'j':j,'waiting_list' : waiting_list,'completed_list' : completed_list,'Prescription_list' :Prescription_list,'curpat':curpat,'history':history,'yest_list':yest_list,'week_list':week_list,'month_list':month_list}
			return render(request,'doctor.html',context)
		elif(request.method == 'POST'):
			crequest = CRequest.objects.filter(doctor__username = username, status='1' ).order_by('appoint_date')[0]
			reg_no = crequest.reg_no
			doctor = crequest.doctor
			disease = request.POST['disease']
			symptoms = request.POST['symptoms']
			next_visit = request.POST['next_visit']
			prescription_time = datetime.datetime.now()
			medicine = str([request.POST['med1'],request.POST['med2'],request.POST['med3'],request.POST['med4'],request.POST['med5']])
			timing = str([request.POST['time1'],request.POST['time2'],request.POST['time3'],request.POST['time4'],request.POST['time5']])
			#assert(False)
			#####add more text boxes 
			obj=Prescription(reg_no=reg_no,doctor=doctor,disease=disease,medicine=medicine,symptoms=symptoms,prescription_time=prescription_time,next_visit=next_visit,medtime=timing)
			obj.save()
			curpat = CRequest.objects.filter(doctor__username = username, status='1' ).order_by('appoint_date')[0]
			curpat.status = '2'
			curpat.save()
			return redirect('/rtc/doctor_home')

@csrf_exempt
@login_required
def waiting_list(request):
	username = request.user.username
	if len(Doctor.objects.filter(username = username)) == 0:
		return render(request, 'error.html', {"error_message": "Only a doctor can access this page!"})
	else:
		now = datetime.datetime.now()
		waiting_list= CRequest.objects.filter(doctor__username = username, status='0',appoint_date__year=now.year,appoint_date__month=now.month,appoint_date__day=now.day ).order_by('appoint_date')
		context = {'waiting_list' : waiting_list}
		return render(request,'waiting_list.html',context)

@csrf_exempt
@login_required
def completed_list(request):
	username = request.user.username
	if len(Doctor.objects.filter(username = username)) == 0:
		return render(request, 'error.html', {"error_message": "Only a doctor can access this page!"})
	else:
		now = datetime.datetime.now()
		completed_list= CRequest.objects.filter(doctor__username = username, status='2',appoint_date__year=now.year,appoint_date__month=now.month,appoint_date__day=now.day ).order_by('appoint_date')
		context = {'completed_list' : completed_list }
		return render(request,'completed_list.html',context)

@csrf_exempt
@login_required
def current_patient(request):
	username = request.user.username
	reg_no=request.POST['reg_no']
	if len(Doctor.objects.filter(username = username)) == 0:
		return render(request, 'error.html', {"error_message": "Only a doctor can access this page!"})
	else:
		patient = Patient.objects.get(reg_no=reg_no);
		#do security here
		context = {'patient': patient }
		return render(request,'current_patient.html',context)

@login_required
def patient_history(request):
	username = request.user.username
	reg_no=request.POST['reg_no']
	if len(Doctor.objects.filter(username = username)) == 0:
		return render(request, 'error.html', {"error_message": "Only a doctor can access this page!"})
	else:
		Prescription_list = Prescription.objects.filter(reg_no__reg_no = reg_no).order_by('appoint_date')
		#do security here
		context = {'Prescription_list': Prescription_list }
		return render(request,'patient_history.html',context)
@csrf_exempt
@login_required
def rec_waiting_list(request):
	username = request.user.username
	if len(Reception.objects.filter(username = username)) == 0:
		return render(request, 'error.html', {"error_message": "Only Reception can access this page!"})
	else:
		now = datetime.datetime.now()
		rec_waiting_list= CRequest.objects.filter(status='0',appoint_date__year=now.year,appoint_date__month=now.month,appoint_date__day=now.day ).order_by('appoint_date')
		context = {'rec_waiting_list' : rec_waiting_list}
		return render(request,'rec_waiting_list.html',context)

@csrf_exempt
@login_required
def rec_completed_list(request):
	username = request.user.username
	if len(Reception.objects.filter(username = username)) == 0:
		return render(request, 'rec_login.html', {"error_message": "Only Reception can access this page!"})
	else:
		now = datetime.datetime.now()
		rec_completed_list= CRequest.objects.filter(status='2', done = False ,appoint_date__year=now.year,appoint_date__month=now.month,appoint_date__day=now.day).order_by('appoint_date')
		context = {'rec_completed_list' : rec_completed_list }
		return render(request,'rec_completed_list.html',context)

@csrf_exempt
@login_required
def rec_pending_list(request):
	username = request.user.username
	if len(Reception.objects.filter(username = username)) == 0:
		return render(request, 'error.html', {"error_message": "Only Reception can access this page!"})
	else:
		now = datetime.datetime.now()
		rec_pending_list= CRequest.objects.filter(status='1',appoint_date__year=now.year,appoint_date__month=now.month,appoint_date__day=now.day).order_by('appoint_date')
		context = {'rec_pending_list' : rec_pending_list }
		return render(request,'rec_pending_list.html',context)


@login_required
def print_prescription(request,tag):
	reg_no=tag
	prescription = Prescription.objects.filter(reg_no__reg_no=reg_no).order_by('prescription_time')[0]
	patient = Patient.objects.get(reg_no= reg_no)

	try: crequest = CRequest.objects.get(reg_no= patient,status= '2')

	except: return redirect('/rtc/reception')
	crequest.done = True
	crequest.save()
	medicine=prescription.medicine
	medicine = medicine.split(',')
	medicine[0] = medicine[0][1:]
	medicine[-1]=medicine[-1][:-1]
	medtime = prescription.medtime
	medtime = medtime.split(',')
	medtime[0] = medtime[0][1:]
	medtime[-1]=medtime[-1][:-1]
	medtime1 = []
	med = []
	for i in range(len(medicine)):
		if medicine[i][2] != '\'':
			med.append(medicine[i][1:-1])
			medtime1.append(medtime[i][1:-1])
	context={'prescription' : prescription,'patient':patient, 'medicine':med, 'medtime':medtime1}

	return render(request,'print2.html',context)


#############################################################################################################
################################Followup Forum#############
#############################################################################################################



@login_required
def f1(request):
	username = request.user.username
	if len(Doctor.objects.filter(username = username)) == 0:
		return render(request, 'error.html', {"error_message": "Only a doctor can access this page!"})
	else:
		username = request.user.username
		follow = FollowUp.objects.filter(doctor__username = username).order_by('patient')
		context = {'FollowUp' : follow}
		return render(request,'docfollowup.html',context)

@login_required
def f1_detail(request, pk):
	username = request.user.username
	if len(Doctor.objects.filter(username = username)) == 0:
		return render(request, 'error.html', {"error_message": "Only a doctor can access this page!"})
	else:
		follow_up = FollowUp.objects.get(pk=pk)
		context = {'followup': follow_up}
		return render(request, 'f1_detail.html', context)

@login_required
def delete(request):
	username = request.user.username
	if len(Doctor.objects.filter(username = username)) == 0:
		return render(request, 'error.html', {"error_message": "Only a doctor can access this page!"})
	else:	
		checks = request.POST.getlist('checks[]')
		checks = map(int,checks)
		#chk = [0,1,2]
		#context = {'chk' : checks}
		#return render(request, 'a1.html', context)
		follow = FollowUp.objects.filter(doctor__username = username).order_by('patient')
		for follow_up in follow:
			if(follow_up.prescription.id in checks):
				follow_up.Doctor_delete = True
				follow_up.save()
		return redirect('../f1')

@login_required
def reply(request, pk):
	username = request.user.username
	if len(Doctor.objects.filter(username = username)) == 0:
		return render(request, 'error.html', {"error_message": "Only a doctor can access this page!"})
	else:
		follow = FollowUp.objects.get(pk=pk)
		follow.Reply_from_doctor = request.POST['textarea']
		follow.save()

	#For testing
	#context = {'s':s}
	#return render(request, 'a1.html', context)


	return redirect('../f1')



@login_required
def followup(request,pres_id=0):
	username = request.user.username
	if len(Patient.objects.filter(username = username)) == 0:
		return render(request, 'error.html', {"error_message": "Only a patient can access this page!"})
	else:
		if request.method == 'GET':
			is_private = request.POST.get('is_private', False)
			patname1=request.user.username
			regno1=Patient.objects.get(username=patname1)
			idval=Patient.objects.get(username=patname1).id
			follow_up=FollowUp.objects.filter(patient=regno1)

			pres= Prescription.objects.filter(reg_no= regno1).order_by('id')

			show_id=[]
			for items in pres:
				pres_date=items.prescription_time

				followup_date=pres_date+datetime.timedelta(days=items.next_visit)
				checktime=timezone.now()
				if (checktime >= followup_date):
					show_id.append(items.id)


			for items in pres:
				pres_date=items.prescription_time

				followup_date=pres_date+datetime.timedelta(days=items.next_visit+30)
				checktime=timezone.now()
				if (checktime >= followup_date):

					show_id.remove(items.id)

			hide_id=[]
	 		for items in follow_up:
	 			hide_id.append(items.prescription.id)
	 			if(items.Patient_delete == True):
	 				show_id.remove(items.prescription.id)





			context={'patname1': patname1,'regno':regno1,'id':'chu','list':pres,'hide':hide_id,'show':show_id,'len':len(pres),'followup':follow_up,'val':''}

			#assert(False)
			return render(request,'followup.html',context)


		elif request.method == 'POST':
			is_private = request.POST.get('is_private', False)
			patname1=request.user.username
			regno1=Patient.objects.get(username=patname1)
			idval=Patient.objects.get(username=patname1).id
			follow_up=FollowUp.objects.filter(patient=regno1)

			pres= Prescription.objects.filter(reg_no= regno1).order_by('id')





			if pres_id != 0:
				pres=Prescription.objects.get(id=pres_id)
				doc=Doctor.objects.get(name=pres.doctor.name)
				title=request.POST['title']
				description=request.POST['description']
				rating= request.POST['rating'].lower()
				# filled=request.POST['filled']

				if (request.POST['rating'] == '' or (title.isalpha() == False  and title != '')):
					if request.POST['rating'] == '':
						messages.success(request, "Rating Cannot be Empty")
					elif (title.isalpha()==False and title != ''):
						messages.success(request, "Title can only contain alphabets")
					

					return HttpResponseRedirect('/rtc/followup/studfollowup/%s' %pres_id )
					#return render(request, 'login.html', {"error_message": 'Atleast one of the given username and password is incorrect.'})
				else:
					response=FollowUp(title=title,description=description,rating=rating,patient=regno1,doctor=doc,prescription=pres,is_filled=True)
					response.save()
					return HttpResponseRedirect('/rtc/followup/')


			elif pres_id == 0:
				#pres_list= Prescription.objects.filter(reg_no= regno1).order_by('id')
				val=request.POST.getlist('to_del')
				val = map(int,val)
				# follow_up=FollowUp.objects.filter(patient=regno1)
				if len(val) > 0:
					for items in pres:
						if items.id in val:
							pres=Prescription.objects.get(id=items.id)
							doc=Doctor.objects.get(name=pres.doctor.name)
							response=FollowUp(title="FollowUp Not Filled",patient=regno1,doctor=doc,prescription=pres,is_filled=True,Patient_delete=True)
							response.save()
				# context={'list':val,'list1':pres,'list2':v}
				# return render(request,'check.html',context)



				#context={'list':val}
				#return render(request,'check.html',context)
				# except:

				# 	return HttpResponseRedirect('/rtc/followup/')


				# except:
				# 	return HttpResponseRedirect('/rtc/followup/')
				#Patient_delete.append(val)

				return HttpResponseRedirect('/rtc/followup/')

@login_required
def studfollowup(request,pres_id=1):
	username = request.user.username
	if len(Patient.objects.filter(username = username)) == 0:
		return render(request, 'error.html', {"error_message": "Only a patient can access this page!"})
	else:
		patname1 = request.user.username
		patname1 = request.user.username
		regno1=Patient.objects.get(username=patname1)
		prescription= Prescription.objects.get(id=pres_id)
		context={'list': prescription}
		return render(request,'studfollowup.html',context)

#####################################################################################################
#####################################################################################################
#####################################################################################################

def med(request):
    if request.method == 'GET':
        context={}
        return render(request,'med/med.html')
    elif request.method == 'POST':
        name1 = request.POST['name']
        name2= request.POST['field']
        if (name2=='1'):
           # meds = Medicine.objects.all().filter(name__contains=name1 )
            meds = Medicine.objects.all().filter(Q(name__contains=name1) | Q(salt__contains=name1))
         
            template = loader.get_template('med/med.html')
            context = RequestContext(request,{'med': meds})
            return HttpResponse(template.render(context))
        else:
            meds = Medicine.objects.all().filter(disease__contains=name1)
            template = loader.get_template('med/med.html')
            context = RequestContext(request,{'med': meds})
            return HttpResponse(template.render(context))
##########################################################################################################
###################################Medicine Search#########################################################
##########################################################################################################
def med(request):
    if request.method == 'GET':
        context={}
        return render(request,'med/med.html')
    elif request.method == 'POST':
        name1 = request.POST['name']
        name2= request.POST['field']
        
        if (name2=='1'):
           # meds = Medicine.objects.all().filter(name__contains=name1 )
            meds = Medicine.objects.all().filter(Q(name__contains=name1) | Q(salt__contains=name1))
            template = loader.get_template('med/med.html')
            context = RequestContext(request,{'med': meds})
            return HttpResponse(template.render(context))
        else:
            meds = Medicine.objects.all().filter(disease__contains=name1)
            template = loader.get_template('med/med.html')
            context = RequestContext(request,{'med': meds})
            return HttpResponse(template.render(context))

@csrf_exempt
def med_search(request):
    if request.method=='POST' :
        search_text=request.POST['value']
        res=Medicine.objects.all().filter(Q(name__contains=search_text) | Q(salt__contains=search_text) )
        temp = loader.get_template('med/med_search.html')
        cont = RequestContext(request,{'re': res})
    else:
        search_text=''
        res=''
        temp = loader.get_template('med/med_search.html')
        cont = RequestContext(request,{'re': res})
   
    return HttpResponse(temp.render(cont))
@csrf_exempt
def dis_search(request):
    if request.method=='POST' :
        search_text=request.POST['value']
        res=Medicine.objects.all().filter(disease__contains=search_text)
        temp = loader.get_template('med/dis_search.html')
        cont = RequestContext(request,{'re': res})
    else:
        search_text=''
        res=''
        temp = loader.get_template('med/dis_search.html')
        cont = RequestContext(request,{'re': res})
    return HttpResponse(temp.render(cont))

########################################################################################################
########################################################################################################
########################################################################################################

#############################################################################################################
################################Insurance Forum#############
#############################################################################################################
@login_required
def main(request):
	username = request.user.username
	if len(Patient.objects.filter(username = username)) == 0:
		return render(request, 'error.html', {"error_message": "Only a patient can access this page!"})
	else:
	    latest_rems = Internal_rim.objects.all().filter(username=username)
	    com=Internal_rim.objects.all().filter(username=username)
	    template = loader.get_template('rtc/main.html')
	    context = RequestContext(request,{'latest_rem': latest_rems,'cn':len(com)})
	    return HttpResponse(template.render(context))

@login_required
def ins_scheme(request):
	username = request.user.username
	if len(Patient.objects.filter(username = username)) == 0:
		return render(request, 'error.html', {"error_message": "Only a patient can access this page!"})
	else:
		return render(request,'rtc/ins_scheme.html')

@login_required
def med_account(request):
	username = request.user.username
	if len(Finance_accountant.objects.filter(username = username)) == 0:
		return render(request, 'error.html', {"error_message": "Only a patient can access this page!"})
	else:
	    req=Internal_rim.objects.filter(status = False)
	    context={'req' : req}
	    return render(request, 'rtc/med_account.html',context)

@login_required
def req_acc(request):
	username = request.user.username
	if len(Finance_accountant.objects.filter(username = username)) == 0:
		return render(request, 'error.html', {"error_message": "Only a patient can access this page!"})
	else:
	    if request.method == 'GET':
	        primary_key=request.GET['pk']
	        rim_objects=Internal_rim.objects.filter(pk=primary_key, status = False)
	        temp="mayank"

	        for obj in rim_objects:
	            exp_part=obj.exp_p
	            temp=exp_part
	            list1=temp.split(':')
	            num=len(list1)
	            exp_amo = obj.exp_amount
	            temp=exp_amo
	            list2=temp.split(':')
	            list3=[]
	        for i in range(num):
	            dic={'part':list1[i], 'amount':list2[i]}
	            list3.append(dic)
	        context={'rim_objects':rim_objects, 'list3':list3,'num':num}
	        return render(request,'rtc/req_acc.html',context)
	    elif request.method == 'POST':
	        a=request.POST['primary_key']
	        rim_amount=request.POST['amount']
	        t_amount=request.POST['t_amount']
	        if rim_amount > t_amount:
	            # return render(request,'rtc/req_acc.html', {"error_message": "Reimburse amount can't be greater than Requested amount"})
	        	redirect('/rtc/med_account')
	        else:
	            rim_object=Internal_rim.objects.filter(pk=a)
	            for obj in rim_object:
	                obj.rim_amount=rim_amount
	                obj.status=True
	                obj.save()
	                req=Internal_rim.objects.filter(status = False)
	                context={'req' : req}
	                return redirect('/rtc/med_account')
@login_required         
def in_rim(request):
	username = request.user.username
	if len(Patient.objects.filter(username = username)) == 0:
		return render(request, 'error.html', {"error_message": "Only a patient can access this page!"})
	else:
	    if request.method == 'GET':
	        context={}
	        return render(request,'rtc/internal_rim.html',context)
	    elif request.method == 'POST':
	        subs=request.POST['sub']
	        patient_name1=request.POST['patient_name']
	        roll_no1=request.POST['roll_no']
	        relationship1=request.POST['relationship']
	        acc_no1=request.POST['acc_no']

	        exp_p1=request.POST['exp_p1']
	        exp_amount1=request.POST['exp_amount1']
	        exp_p2=request.POST['exp_p2']
	        exp_amount2=request.POST['exp_amount2']
	        if not exp_p2 == "":
	            exp_p1=exp_p1 + ":" + exp_p2
	            exp_amount1=exp_amount1 + ":" + exp_amount2

	        exp_p3=request.POST['exp_p3']
	        exp_amount3=request.POST['exp_amount3']
	        if not exp_p3 == "":
	            exp_p1=exp_p1 + ":" + exp_p3
	            exp_amount1=exp_amount1 + ":" + exp_amount3

	        exp_p4=request.POST['exp_p4']
	        exp_amount4=request.POST['exp_amount4']
	        if not exp_p4 == "":
	            exp_p1=exp_p1 + ":" + exp_p4
	            exp_amount1=exp_amount1 + ":" + exp_amount4

	        
	        t_amount1=request.POST['t_amount']
	        obj=Internal_rim(username=username,subject=subs, patient_name=patient_name1,roll_no=roll_no1,relationship=relationship1,acc_no=acc_no1,exp_p=exp_p1,exp_amount=exp_amount1,t_amount=t_amount1,rec_time=datetime.datetime.now())
	        obj.save()
	        return redirect('/rtc/main')


#############################################################################################################
#############################################################################################################
#############################################################################################################