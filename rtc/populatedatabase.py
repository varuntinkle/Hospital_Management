from database.models import CRequest,Medicine,FollowUp,Complaint,Doctor,Prescription,Reception,Patient
from os.path import abspath, exists
import os
from django.contrib.auth.models import User


# workpath = os.path.dirname(os.path.abspath(__file__)) #Returns the Path your .py file is in
i=1
while i<15:
	username="doc"+str(i)
	name="Dr Doctor"+str(i)
	obj=Doctor(username=username,name=name)
	obj.save()
	# obj=User(username=username,password="pass")
	# obj.save()
	i=i+1

workpath=os.getcwd()
f = open(os.path.join(workpath, 'rtc/patients.txt'), 'r')

i=1
for line in f.readlines():

	# whiteSpaceRegex = "\\s"	
	# words = line.split(whiteSpaceRegex)
	words = line.split()
	username="pat"+str(i)
	reg_no="s"+str(i)
	name=words[2]
	obj=Patient(username=username,reg_no=reg_no,name=name,age=19,height=172,weight=50)
	obj.save()
	# obj=User(username=username,password="pass")
	# obj.save()
	i=i+1
	myStr = "2015-10-01 15:26:13"
	myStr1 = "2015-13-01 15:26:13"

	# if i < 15:
	# 	doc="doc"+str(i)
	# 	reg_no = Patient.objects.get(reg_no=reg_no)
	# 	if i > 15:
	# 		j = i/15
	# 	else:
	# 		j = i
	# 	doctor = Doctor.objects.get(username="doc"+str(j))
	# 	obj=CRequest(name=name,reg_no=reg_no,problem="fever",request_date=myStr,appoint_date=myStr,	appoint_no=i,doctor=doctor,status="1")
	# 	obj.save()


f.close()
workpath=os.getcwd()
f = open(os.path.join(workpath, 'rtc/medicines.txt'), 'r')

for line in f.readlines():
	i=100
	if i < 200:
		obj=Medicine(name=line,mg=200,price=i,prsc_required=0)
		obj.save()

	else:	
		obj=Medicine(name=line,mg=200,price=i,prsc_required=1)
		obj.save()

	i=i+1
	


		