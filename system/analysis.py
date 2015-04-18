#####NIkit Prabodh########
import math
import datetime
from database.models import Prescription, Doctor, Registration, FollowUp
import nltk

def disease(diseasename):
	quan = 0
	Object_Searched = Prescription.objects.all()
	month = [0]*12
	diseasesearch = diseasename
	for i in Object_Searched:
		#print i.medicine
		#print len(i.disease)
		
		print (i.prescription_time.month)
		val = i.disease.lower().find(diseasesearch.lower())
		if val !=-1 :
			month[i.prescription_time.month-1] = month[i.prescription_time.month-1] + 1
			print (month)	
	return month
	#month val
	#print quan

def medicine(medicinename):
	quan = 0
	Object_Searched = Prescription.objects.all()
	print (Object_Searched)
	month = [0]*12
	medicinesearch = medicinename
	for i in Object_Searched:
		#print
		#print i.medicine.all()
		
			val = i.medicine.lower().find(medicinesearch.lower())
			if val !=-1 :
				month[i.prescription_time.month-1] = month[i.prescription_time.month-1] + 1
	return month

def medicineword():
	quan = 0
	Object_Searched = Prescription.objects.all()
	#print (Object_Searched)
	words = {}

	#medicinesearch = medicinename
	for i in Object_Searched:
		#print
		#print i.medicine.all()
		temp = []
		temp = i.medicine
		temp = temp.replace('u',' ')
		temp = temp.replace(',',' ')
		temp = temp.replace('[',' ')
		temp = temp.replace(']',' ')
		temp = temp.replace('\'',' ')
		
		
		toks = nltk.word_tokenize(temp)
		for w in toks:
			w = w.lower()
			if w != "and":
				if w in words:
					words[w] += 1
				else:
					words[w] = 1
	
	return words

def diseaseword():
	Object_Searched = Prescription.objects.all()
	words = {}
	for i in Object_Searched:
		toks = nltk.word_tokenize(i.disease)
		for w in toks:
			w = w.lower()
			if w != "and":
				if w in words:
					words[w] += 1
				else:
					words[w] = 1

	return words


def diseaseword_timelimit(startdate, enddate):
	start = datetime.datetime.strptime(startdate, '%Y-%m-%d').date()
	end = datetime.datetime.strptime(enddate, '%Y-%m-%d').date()
	Object_Searched = Prescription.objects.all()
	words = {}
	for i in Object_Searched:
		if (start < i.prescription_time.date() < end):
			toks = nltk.word_tokenize(i.disease)
			for w in toks:
				w = w.lower()
				if w != "and":
					if w in words:
						words[w] += 1
					else:
						words[w] = 1

	return words

def medicineword_timelimit(startdate, enddate):
	start = datetime.datetime.strptime(startdate, '%Y-%m-%d').date()
	end = datetime.datetime.strptime(enddate, '%Y-%m-%d').date()
	quan = 0
	Object_Searched = Prescription.objects.all()
	#print (Object_Searched)
	words = {}
	
	#medicinesearch = medicinename
	for i in Object_Searched:
		#print
		#print i.medicine.all()
		if (start < i.prescription_time.date() < end):
			temp = []
			temp = i.medicine
			temp = temp.replace('u',' ')
			temp = temp.replace(',',' ')
			temp = temp.replace('[',' ')
			temp = temp.replace(']',' ')
			temp = temp.replace('\'',' ')
			
			toks = nltk.word_tokenize(temp)
			for w in toks:
				w = w.lower()
				if w != "and":
					if w in words:
						words[w] += 1
					else:
						words[w] = 1

	return words

def disease_timelimit(diseasename, startdate, enddate):
	start = datetime.datetime.strptime(startdate, '%Y-%m-%d').date()
	end = datetime.datetime.strptime(enddate, '%Y-%m-%d').date()
	quan = 0
	Object_Searched = Prescription.objects.all()
	month = [0]*12
	diseasesearch = diseasename
	for i in Object_Searched:
		#print i.medicine
		#print len(i.disease)
		
		#print (i.prescription_time.month)
		val = i.disease.lower().find(diseasesearch.lower())
		if (val !=-1) and (start < i.prescription_time.date() < end):
			month[i.prescription_time.month-1] = month[i.prescription_time.month-1] + 1
			print (month)
	return month
def medicine_timelimit(medicinename, startdate, enddate):
	start = datetime.datetime.strptime(startdate, '%Y-%m-%d').date()
	end = datetime.datetime.strptime(enddate, '%Y-%m-%d').date()
	quan = 0
	Object_Searched = Prescription.objects.all()
	print (Object_Searched)
	month = [0]*12
	medicinesearch = medicinename
	for i in Object_Searched:
		#print
		#print i.medicine.all()
		for j in i.medicine.all():

			val = j.name.lower().find(medicinesearch.lower())
			if val !=-1 and (start < i.prescription_time.date() < end):
				month[i.prescription_time.month-1] = month[i.prescription_time.month-1] + 1
	return month



def prescription_analysis():
	rating_array = [0]*5
	all_prescriptions = FollowUp.objects.all()
	for i in all_prescriptions:
		rating_array[int(i.rating) - 1] = rating_array[int(i.rating) - 1] + 1
		print (i.rating)
	#print (rating_array)
	return rating_array


def prescription_analysis_word():
	Object_Searched = FollowUp.objects.all()
	words = {}
	for i in Object_Searched:
		toks = nltk.word_tokenize(i.description)
		for w in toks:
			w = w.lower()
			if w != "and":
				if w in words:
					words[w] += 1
				else:
					words[w] = 1
	return words


def prescription_analysis_timelimit(startdate, enddate):
	start = datetime.datetime.strptime(startdate, '%Y-%m-%d').date()
	end = datetime.datetime.strptime(enddate, '%Y-%m-%d').date()
	quan = 0
	Object_Searched = FollowUp.objects.all()
	print (Object_Searched)
	rating_array = [0]*5
	#medicinesearch = medicinename
	for i in Object_Searched:
		#print
		#print i.medicine.all()
		if( start < i.prescription.prescription_time.date() < end) :
			rating_array[int(i.rating) - 1] = rating_array[int(i.rating) - 1] + 1
		print (i.rating)
	return rating_array


def prescription_analysis_word_timelimit(startdate, enddate):
	start = datetime.datetime.strptime(startdate, '%Y-%m-%d').date()
	end = datetime.datetime.strptime(enddate, '%Y-%m-%d').date()
	Object_Searched = FollowUp.objects.all()
	words = {}
	for i in Object_Searched:
		if (start < i.prescription.prescription_time.date() < end):
			toks = nltk.word_tokenize(i.description)
			for w in toks:
				w = w.lower()
				if w != "and" and w != "the" and w != "is":
					if w in words:
						words[w] += 1
					else:
						words[w] = 1

	return words
#####end NIkit Prabodh########
		
