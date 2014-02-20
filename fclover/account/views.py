# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.models import User
from django.template import RequestContext

def signup(request):
    return render_to_response('signup.html', context_instance=RequestContext(request))

def signin(request):
    return render_to_response('signin.html', context_instance=RequestContext(request))
