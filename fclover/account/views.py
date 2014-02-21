# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.models import User
from django.template import RequestContext
from fclover.account.forms import SigninForm
from fclover.account.models import UserProfile
from django.contrib.auth import authenticate

def signup(request):
    return render_to_response('account/signup.html', context_instance=RequestContext(request))

def signin(request):
    if request.method == 'POST':
        form = SigninForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            return HttpResponse('Welcome back!')
    else:
        form = SigninForm()
    return render_to_response('account/signin.html', {'form': form},context_instance=RequestContext(request))
