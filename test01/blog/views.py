from django.shortcuts import render, render_to_response
from django.http.response import HttpResponse
import datetime

# Create your views here.
def hello(request):
    return HttpResponse("hello world")

def date(request):
    now = datetime.datetime.today()
    return render_to_response('blog/current_datetime.html', locals())

def current_datetime(request):
    date = datetime.datetime.now()      
    return render_to_response('blog/current_datetime.html',{'current_date': date})

def hours_ahead(request, offset):
    try:
       offset = int(offset)
    except ValueError:
       raise Http404()
    assert False
    now = datetime.datetime.today()
    new_time = now + datetime.timedelta(hours=offset)    
    return render_to_response('blog/hours_ahead.html', locals())

def thanks(request):
    user = 'root'
    currentuser = 'roo'
    ship_date = datetime.date(2016, 12, 12)
    person_name = 'marry'
    athlete_list = ['Tank', 'stef', 'David', 'John']
    #athlete_list = []
    contact = {'tom': '1244', 'hellen': '34344', 'max': '3344'}
    item_list = ['apple', 'trawberry', 'banana']   
    return render_to_response('blog/thanks.html', locals())