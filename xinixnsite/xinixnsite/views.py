from django.http import HttpResponse
import datetime
from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response
import MySQLdb
from django.http.request import HttpRequest




def hello(request):
    return HttpResponse("Hello worldsss")


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

def book_list(request):
    db = MySQLdb.connect(user='me', db='mydb', passwd='secret', host='localhost')
    cursor = db.cursor()
    cursor.execute('select name FROM books ORDER BY name')
    names = [row[0] for row in cursor.fetchall()]
    db.close()
    return render_to_response('book_list.html',{'names': names})

def current_url_view(request):
    return HttpResponse("welcome to the page at %s" % request.path)

def display_meta(request):
    values = request.META.items()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))


    
