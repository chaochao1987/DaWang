from django.http import HttpResponse, Http404
import datetime
def hello(request):
    return HttpResponse("welcome to my site")

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html ="<html><body>In %s hour(s),it will be %s </body></html>" % (offset, dt)
    return HttpResponse(html)

def time(request, year, month):
    html = "you input year: %s and month: %s " % (year, month)
    return HttpResponse(html)
