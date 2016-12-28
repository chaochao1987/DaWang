from django.shortcuts import render, render_to_response
from django.http.response import HttpResponse, HttpResponseRedirect
from blog.models import Book

# Create your views here.
def hello(request):
    return HttpResponse("welcome to the page at %s" % request.path)

def ua_display_good1(request):
    try:
        ua = request.META['HTTP_REFERER']
    except keyError:
        ua = 'unknown'        
    return HttpResponse("Your browser is %s" % ua)

def ua_display_good2(request):
    ua = request.META.get('ua', 'unknown')
    return HttpResponse("Your browser is %s " % ua)

def display_meta(request):
        return render_to_response('index.html',locals())
# str ="-"
# seq = ['a', 'b', 'c']
#pirnt str.join(seq)
# a-b-c 

def search_form(request):
    return render_to_response('search_form.html')

def search(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Enter a search term.')
        elif len(q) > 20:
            errors.append('Please enter at most 20 characters.')
        else:
            return render_to_response('search_results.html',locals())
    return render_to_response('search_form.html', locals())
    
def bad_search(request):
    # The following line will raise KeyError if 'q' hasn't
    # been submitted!
    message = 'You searched for: %r' % request.GET['q']
    return HttpResponse(message)

def thanks(request):
    return render_to_response('thanks.html',{
        
    })


            