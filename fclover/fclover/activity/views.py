# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.models import User
from django.template import RequestContext

from fclover.activity.models import Activity

def index(request):
    activity_list = Activity.objects.all().order_by('-createTime')
    return render_to_response('index.html', {'activity_list': activity_list}, context_instance=RequestContext(request))

def create(request):
    if request.POST.__len__() == 0:
        return render_to_response('activity/create.html', context_instance=RequestContext(request))
    else:
        title = request.POST['title']
        content = request.POST['content']
        picture = request.POST['picture']
        createTime = request.POST['createTime']
        dueTime = request.POST['dueTime']
        beginTime = request.POST['beginTime']
        endTime = request.POST['endTime']
        location = request.POST['location']
        maxMale = request.POST['maxMale']
        maxFemale = request.POST['maxFemale']
        type = request.POST['type']
        user_id = reqeust.POST['user_id']
        act = Activity(title = title, picture = picture, content = content, createTime = createTime, dueTime = dueTime, beginTime = beginTime, endTime = endTime, location = location, maxMale = maxMale, maxFemale = maxFemale, type = type, initiator_id = user_id)
        # TODO check all parameters
        if check_parameter(act):
            act.save()
            # TODO save activity object
            return HttpResponseRedirect(reverse('fclover.activity.views.index', None))
        else:
            return render_to_response('activity/create.html', {"message": "parameter wrong"}, context_instance=RequestContext(request))


def delete(request):
    return
