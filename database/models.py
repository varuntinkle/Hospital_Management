from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User



class CRequest(models.Model):
	status_choice=(('0','Waiting'),('1','Pending'),('2','Completed'))
	name = models.CharField(max_length = 140)
	reg_no = models.ForeignKey('Patient',null= True,blank=True)
	problem= models.CharField(max_length = 140)
	request_date = models.DateTimeField()
	appoint_date = models.DateTimeField()
	appoint_no = models.IntegerField()
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
	prsc_required = models.BooleanField(default = False)
	def __unicode__(self):
		return self.name

class FollowUp(models.Model):
	# rating=(('1','poor'),('2','Average'),('3','good'),('4','very good'),('5','excellent'))
	# patient = models.ForeignKey('Patient')
	# doctor = models.ForeignKey('Doctor')
	# title = models.CharField(max_length=200)
	# description = models.TextField(blank=True)
	# rating = models.CharField(max_length=1,choices=rating)
	################################################3
	prescription = models.OneToOneField('Prescription', primary_key=True)
	# expiry_date = models.DateField()
	# new addition : is_filled
	is_filled=models.BooleanField(default=False)
	rating=(('1','poor'),('2','Average'),('3','good'),('4','very good'),('5','excellent'))
	patient = models.ForeignKey('Patient')
	doctor = models.ForeignKey('Doctor')
	title = models.CharField(max_length=200)
	description = models.CharField(max_length=1000)
	rating = models.CharField(max_length=1,choices=rating)
	def __unicode__(self):
		return self.title
	################################################3

class Complaint(models.Model):
	category=(('1','poor'),('2','Average'),('3','good'),('4','very good'),('5','excellent'))
	username = models.CharField(max_length=140)
	category = models.CharField(max_length=10,choices=category)
	subject = models.CharField(max_length=140)
	complaint = models.TextField(blank=True)
	complaint_date = models.DateTimeField()
	doc_pat = models.BooleanField(default=0)
	def __unicode__(self):
		return self.subject

class Prescription(models.Model):
	reg_no = models.ForeignKey('Patient')
	doctor = models.ForeignKey('Doctor')
	disease = models.CharField(max_length = 256)
	medicine = models.TextField('Medicine')#########change########
	symptoms = models.TextField(blank = True)
	prescription_time = models.DateTimeField(blank=True)
	next_visit = models.IntegerField(unique = False,null= True,blank=True)
	def __str__(self):
		return self.disease
		
class Registration(models.Model):
	username = models.CharField(max_length=20)
	password = models.CharField(max_length=100)
	name = models.CharField(max_length=20)
	category=models.IntegerField()
	def __str__(self):
		return self.username+"*"+self.password+"*"+self.name

class Doctor(models.Model):
	username = models.CharField(max_length=30)
	name = models.CharField(max_length = 50)
	speciality = models.CharField(max_length = 100)
	qualification = models.CharField(max_length = 100)
	patients_visited=models.TextField()
	schedule = models.TextField()
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
	def __str__(self):
		return self.username

	def __str__(self):
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

	


