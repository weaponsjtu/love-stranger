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
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            # Correct password, and the user is marked "active"
            auth.login(request, user)
            # Redirect to a success page.
            return HttpResponse("account/loggedin")
        else:
            # Show an error page
            return render_to_response('account/signin.html', {'form': form, 'invalid': True}, context_instance=RequestContext(request))
    else:
        form = SigninForm()
    return render_to_response('account/signin.html', {'form': form},context_instance=RequestContext(request))
