#####NIkit Prabodh########
from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse
from system.analysis import disease, medicine,medicine_timelimit,medicineword_timelimit, diseaseword,medicineword, disease_timelimit,diseaseword_timelimit, prescription_analysis, prescription_analysis_word ,prescription_analysis_timelimit, prescription_analysis_word_timelimit
import operator, datetime
from collections import OrderedDict


def graphindex(request):
   request.session["fav_color"] = "blue"
   context = RequestContext(request)
   return render_to_response('system/graphindex.html', context)

def graphdisease(request ):
   # varName=request.GET.get('diseasename', '')
	#if varName == '':
	#	return render(request, 'unsuccessfulHack.html', {"error_msg": "Please specify a course"})
	diseasename = request.POST['diseaseinput']
	a=disease(diseasename)
	total =0
	for i in a:
		total = total + i
	avg = total/12
	#str1 = "fever"
	words = diseaseword()
	words_sorted_by_value = dict(sorted(words.iteritems(), key=operator.itemgetter(1), reverse=True)[:5])
	#words_sorted_by_value = OrderedDict(sorted(words.items(), key=lambda x: x[1], reverse=True))
	#b=dataAnalytics.getOverall(courseName)
	#print a, "b", b
	#print "hello"
	#print a
	#assert(False)
	return render(request, 'system/graphdisease.html', {"data": a,"avg":avg,"total":total,"data2": words_sorted_by_value,"data3":words,"disease": diseasename})


def graphmedicine(request ):
   # varName=request.GET.get('diseasename', '')
	#if varName == '':
	#	return render(request, 'unsuccessfulHack.html', {"error_msg": "Please specify a course"})
	medicinename = request.POST['medicineinput']
	a=medicine(medicinename)
	total =0
	for i in a:
		total = total + i
	avg = total/12
	
	words = medicineword()
	words_sorted_by_value = dict(sorted(words.iteritems(), key=operator.itemgetter(1), reverse=True)[:5])
	
	#b=dataAnalytics.getOverall(courseName)
	#print a, "b", b
	#print "hello"
	print (a)
	#assert(False)
	return render(request, 'system/graphmedicine.html', {"data": a,"avg":avg,"total":total,"data2": words_sorted_by_value,"data3": words,"medicine": medicinename})

def graphmedicine_timelimit(request):

	startdate = request.POST['startdatemed_input']
	enddate = request.POST['enddatemed_input']
	medicinename = request.POST['medicineinput']
	c=medicine_timelimit(medicinename,startdate,enddate)
	total =0
	for i in c:
		total = total + i
	avg = total/12
	
	words = medicineword_timelimit(startdate, enddate)
	words_sorted_by_value = dict(sorted(words.iteritems(), key=operator.itemgetter(1), reverse=True)[:5])
	
   # varName=request.GET.get('diseasename', '')
	#if varName == '':
	#	return render(request, 'unsuccessfulHack.html', {"error_msg": "Please specify a course"})
	
	
	
	#b=dataAnalytics.getOverall(courseName)
	#print a, "b", b
	#print "hello"
	
	#assert(False)
	return render(request, 'system/graphmedicine.html', {"data": c,"avg":avg,"total":total,"medicine": medicinename,"data2":words_sorted_by_value,"data3":words})

def diseasewordcloud(request):

	words = diseaseword()

	return render(request, 'system/diseasewordcloud.html', {"data": words})

def graphdisease_timelimit(request):
	startdate = request.POST['startdate_input']
	enddate = request.POST['enddate_input']
	diseasename = request.POST['diseaseinput']
	c=disease_timelimit(diseasename,startdate,enddate)
	total =0
	for i in c:
		total = total + i
	avg = total/12
	
	words = diseaseword_timelimit(startdate, enddate)
	words_sorted_by_value = dict(sorted(words.iteritems(), key=operator.itemgetter(1), reverse=True)[:5])
	

	print (c)
	return render(request,'system/graphdisease.html',{"data":c,"avg":avg,"total":total,"disease":diseasename, "data2":words_sorted_by_value,"data3":words})
def choosefunctionmed(request):
	try:
		k = request.session["fav_color"]
		startdate = request.POST['startdatemed_input']
		enddate = request.POST['enddatemed_input']
		#request.session["fav_color"] = "blue"
		try:
			datetime.datetime.strptime(startdate, '%Y-%m-%d')
			datetime.datetime.strptime(enddate, '%Y-%m-%d')
			return graphmedicine_timelimit(request)
			
		except ValueError:	
			#raise ValueError("Incorrect data format, should be YYYY-MM-DD")
			return graphmedicine(request)
	except KeyError:
		return render(request, 'system/visit_graphindex.html')

def choosefunction(request):
	try:
		k = request.session["fav_color"]
		startdate = request.POST['startdate_followup_input']
		enddate = request.POST['enddate_followup_input']
		try:
			datetime.datetime.strptime(startdate, '%Y-%m-%d')
			datetime.datetime.strptime(enddate, '%Y-%m-%d')
			return graphdisease_timelimit(request)
			
		except ValueError:	
			#raise ValueError("Incorrect data format, should be YYYY-MM-DD")
			return graphdisease(request)
	except KeyError:
		return render(request, 'system/visit_graphindex.html')


def graphfollowup_timelimit(request):
	startdate = request.POST['startdate_followup_input']
	enddate = request.POST['enddate_followup_input']
	#diseasename = request.POST['diseaseinput']
	c = prescription_analysis_timelimit(startdate,enddate)
	#total =0
	#for i in c:
	#	total = total + i
	#avg = total/12
	
	words = prescription_analysis_word_timelimit(startdate, enddate)
	words_sorted_by_value = dict(sorted(words.items(), key=operator.itemgetter(1), reverse=True)[:5])
	return render(request,'system/graphfollowup.html',{"data":c,"data2":words_sorted_by_value,"data3":words})


def graphfollowup(request):
	try:
		k=request.session["fav_color"]
		d = prescription_analysis()
		print (d)
		words = prescription_analysis_word()
		words_sorted_by_value = dict(sorted(words.items(), key=operator.itemgetter(1), reverse=True)[:5])
		return render(request, 'graphfollowup.html', {"data": d,"data2": words_sorted_by_value,"data3":words})
		#return render(request, 'graphfollowup.html',{"data":d})
	except KeyError:
		return render(request, 'system/visit_graphindex.html')




def choosefunction_followup(request):
	try:
		k = request.session["fav_color"]
		startdate = request.POST['startdate_followup_input']
		enddate = request.POST['enddate_followup_input']
		try:
			datetime.datetime.strptime(startdate, '%Y-%m-%d')
			datetime.datetime.strptime(enddate, '%Y-%m-%d')
			return graphfollowup_timelimit(request)
			
		except ValueError:	
			#raise ValueError("Incorrect data format, should be YYYY-MM-DD")
			return graphfollowup(request)
	except KeyError:
		return render(request, 'system/visit_graphindex.html')
#####end NIkit Prabodh########