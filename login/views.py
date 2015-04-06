#from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse
from database.models import Registration
import django.contrib.auth.hashers 
# Create your views here.

def index(request):
    # Request the context of the request.
    # The context contains information such as the client's machine details, for example.
    context = RequestContext(request)
    return render_to_response('login/login.html', context)


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
                request.session["id"]=Object_Searched.username
                if  Category==1:
                    context = RequestContext(request)
                    message= "Hi1"
                    #return HttpResponse(message)
                    #return HttpResponse(Category)
                    return render_to_response('Doctor_login/index.html', context)
                else:
                    message= "Hi"
                    return HttpResponse(message)

            else:
                message = "Wrong Password"
                return HttpResponse(message)  
        else:
            message="Wrong Username"
            return HttpResponse(message)

