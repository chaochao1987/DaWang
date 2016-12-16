from django.http import HttpResponse
import datetime
from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response



def hello(request):
    return HttpResponse("Hello world")


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    #html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    
    return render_to_response('dateapp/headhour.html', {'hour_offset': offset,'next_time': dt})
    
def current_datetime(request):
    date = datetime.datetime.now()      
    return render_to_response('dateapp/current_datetime.html',{'current_date': date})