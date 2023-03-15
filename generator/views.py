from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import random 
import string

def home(request):
    return render(request,'generator/home.html',{'password':'jkwbreghn'})




def about(request):
    return render( request,'generator/about.html')


def password(request):
        
    charac=list("abcdefghijklmnopqrxtuvwxyz")

    if request.GET.get('uppercase') == 'on':

        charac += string.ascii_uppercase
        #charac.extend(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")) 
    if  request.GET.get('numbers') == 'on':
        charac += string.digits

    if  request.GET.get('special') == 'on':
        ## charac += string.puntuation 
        charac.extend(list("!@#$%^&*")) 


    length=int(request.GET.get("length",14))

    thepassword = ''

    for x  in range(length):
        thepassword += random.choice(charac)

        
    #thepassword= 'testing'
    return render( request,"generator/password.html", {'password':thepassword})





