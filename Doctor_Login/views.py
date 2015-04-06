from django.shortcuts import render

# Create your views here.

def homepage(request):
    # Request the context of the request.
    # The context contains information such as the client's machine details, for example.
  	#if not request.session["member_id"]:
  	#	logout(request)
    
    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    message="Hi"
    return HttpResponse( message )
    return render_to_response('login/index.html', context_dict, context)







def logout(request):
	if request.session["member_id"]:
		del request.session["member_id"]
	return HttpResponse("You're logged out.")
