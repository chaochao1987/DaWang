from django.shortcuts import render, render_to_response
from django.http.response import HttpResponse
import datetime

# Create your views here.
def hello(request):
    return HttpResponse("hello world")

def date(request):
    now = datetime.datetime.today()
    year = now.year
    month = now.month
    day = now.day
    html = "<h1>it's time now: %s/%s/%s</h>" % (year, month, day)
    return HttpResponse(html)

def hours_ahead(request, offset):
    try:
       offset = int(offset)
    except ValueError:
       raise Http404()
    assert False
    now = datetime.datetime.today()
    new_time = now + datetime.timedelta(hours=offset)
    html = "<h1>In %s hours ,it will be %s</h1>" % (offset, new_time)
    return HttpResponse(html)

def thanks(request):
    contact = {'tom': '1244', 'hellen': '34344', 'max': '3344'}
    item_list = ['apple', 'trawberry', 'banana']   
    return render_to_response('blog/thanks.html', {'person_name': 'marry', 'ship_date': datetime.date(2016, 12, 12), \
                'company': 'huishi technology', 'item_list': item_list, 'ordered_warranty': True, 'contact': contact})