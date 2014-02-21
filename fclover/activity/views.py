# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.models import User
from django.template import RequestContext

from activity.models import Activity

def index(request):
    activity_list = Activity.objects.all().order_by('-createTime')
    return render_to_response('index.html', {'activity_list': activity_list}, context_instance=RequestContext(request))


