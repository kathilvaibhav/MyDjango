from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render,render_to_response, RequestContext, HttpResponseRedirect
# Create your views here.
from .forms import SignUpForm

def home(request):
    form = SignUpForm(request.POST or None)    
    if form.is_valid():
        save_it = form.save(commit=False)
        messages.success(request, 'We Will be in touch......')
        save_it.save()
        to_list = ['vaibhav.guptaa@markit.com']
        #send email....        
        send_mail('Hey Test','Jango Test',settings.EMAIL_HOST_USER,to_list,fail_silently=False)
        return HttpResponseRedirect('thankyou')
        
    return render_to_response("signup.html",locals(),context_instance=RequestContext(request))


def thankyou(request):    
    return render_to_response("thanksyou.html",locals(),context_instance=RequestContext(request))

def aboutus(request):    
    return render_to_response("aboutus.html",locals(),context_instance=RequestContext(request))