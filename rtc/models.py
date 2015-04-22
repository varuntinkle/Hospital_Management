from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
import base64
import hashlib
import time


class CRequest(models.Model):
	status_choice=(('0','Waiting'),('1','Pending'),('2','Completed'))
	name = models.CharField(max_length = 140)
	reg_no = models.ForeignKey('Patient',null= True,blank=True)
	problem= models.CharField(max_length = 140)
	request_date = models.DateTimeField()
	appoint_date = models.DateTimeField()
	appoint_no = models.IntegerField(unique = False)
	doctor = models.ForeignKey('Doctor')
	done = models.BooleanField(default = False)
	outsider = models.BooleanField(default= False)
	status =  models.CharField(max_length=1 ,choices=status_choice)
	def __unicode__(self):
		return self.name
	#timing required for online request	

class Medicine(models.Model):
	name = models.CharField(max_length=140)
	salt = models.TextField(blank=True) 
	mg = models.IntegerField()
	price = models.FloatField()
	disease = models.TextField(blank=True)
	misc = models.TextField(blank=True)
	prsc_required = models.BooleanField()
	def __unicode__(self):
		return self.name

class FollowUp(models.Model):
	prescription = models.OneToOneField('Prescription', primary_key=True)
	is_filled=models.BooleanField(default=False)
	rating=(('poor','1'),('average','2'),('good','3'),('very good','4'),('excellent','5'))#conflict with what we are storing
	patient = models.ForeignKey('Patient')
	doctor = models.ForeignKey('Doctor')
	title = models.CharField(max_length=200)
	description = models.CharField(max_length=1000)
	rating = models.CharField(max_length=15,choices=rating)
	Doctor_delete = models.BooleanField(default=False)
	Patient_delete = models.BooleanField(default=False)
	Reply_from_doctor = models.TextField(blank=True)

	def __unicode__(self):
		return self.title

class Complaint(models.Model):
	username = models.CharField(max_length=140)
	category = models.CharField(max_length=20)
	subject = models.CharField(max_length=140)
	complaint = models.TextField(blank=True)
	complaint_date = models.DateTimeField()
	process = models.CharField(max_length=50 ,default='not_seen')
	doc_pat = models.BooleanField(default=0)
	admintext = models.CharField(max_length=140)

	def __str__(self):
		return self.subject

class Prescription(models.Model):
	reg_no = models.ForeignKey('Patient')
	doctor = models.ForeignKey('Doctor')
	disease = models.CharField(max_length = 256)
	medicine = models.TextField('Medicine')#########change########
	symptoms = models.TextField(blank = True)
	prescription_time = models.DateTimeField(blank=True)
	medtime = models.TextField(blank = True,null=True)
	next_visit = models.IntegerField(unique = False,null= True,blank=True)

class Doctor(models.Model):
	username = models.CharField(max_length = 255)
	name = models.CharField(max_length = 20)
	#integrate
	speciality = models.CharField(max_length=100,blank=True)
	qualification = models.CharField(max_length=100,blank=True)
	patients_visited = models.TextField(blank=True)
	schedule = models.TextField(blank=True)
	image=models.FileField(upload_to="./",blank=True)
	#inetgrate
	def __unicode__(self):
		return self.name

class Patient(models.Model):
	username = models.CharField(max_length = 255)
	reg_no = models.CharField(max_length = 10)
	name = models.CharField(max_length = 20)
	age = models.IntegerField()
	height = models.CharField(max_length = 100)
	weight = models.IntegerField(blank = True)
	patient_history = models.TextField(blank=True)
	patient_test = models.TextField(blank=True)
	image = models.FileField(upload_to="./", blank=True)
	def __str__(self):
		return self.username

	def __unicode__(self):
		return self.reg_no
class AmbulanceBooking(models.Model):
	Source = models.CharField(max_length=50)
	Destination = models.CharField(max_length=50)
	DateBooked = models.DateTimeField('Date booked')
	Purpose = models.CharField(max_length=200)
	Day = models.CharField(max_length=9)
	Time = models.TimeField()

class AmbulanceSchedule(models.Model):
	Day = models.CharField(max_length=9)
	Time = models.TimeField()
	Availability = models.BooleanField()
	Count = models.IntegerField()
	def __str__(self):
		return "Day-"+str(self.Day)+", Time-"+str(self.Time)+", Availability-"+str(self.Availability)+", Count-"+str(self.Count)

class Post(models.Model):
    title=models.CharField(max_length=140)
    body = models.TextField()
    date = models.DateTimeField()

    def __unicode__(self):
        return self.title

class Reception(models.Model):
	username = models.CharField(max_length = 255)
        name =models.CharField(max_length = 255)
	image = models.FileField(upload_to="./", blank=True)

	############insurance
class Internal_rim(models.Model):
    username = models.CharField(max_length = 255)
    roll_no = models.CharField(max_length = 10)
    relationship= models.CharField(max_length=50, blank=True)
    patient_name= models.CharField(max_length=255,default='Self')
    acc_no= models.CharField(max_length=50)
    exp_p=models.TextField()
    exp_amount= models.TextField()
    t_amount= models.CharField(max_length=6)
    rim_amount= models.FloatField(max_length=10, default=0)
    status= models.BooleanField(default=False)
    subject=models.CharField(max_length=255)
    rec_time = models.DateTimeField()
    def __unicode__(self):
		return self.username

class Finance_accountant(models.Model):
	username = models.CharField(max_length = 255)
