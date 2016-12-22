from django.http import HttpResponse
from django.shortcuts import render_to_response
from books.models import Book
from django.core.mail import send_mail
from django.http.response import HttpResponseRedirect

def hello(request):
    return HttpResponse("hello world")

def display_meta(request):
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append("<tr><td>%s</td><td>%s</td></tr>" % (k, v))
    return HttpResponse("<table>%s</table>" % '\n'.join(html))

def search_form(request):
    return render_to_response('book/search_form.html')

"""def search(request):
    if 'q' in request.GET:
        message = 'You searched for: %s' % request.GET['q']
    else:
        message = 'You submitted an empty form'
    return HttpResponse(message)"""

def search(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Enter a search term.')
        elif len(q) > 20:
            errors.append('Please enter at most 20 characters.')
        else:
             books = Book.objects.filter(title__icontains=q)
             return render_to_response('book/search_results.html',{'books': books,'query': q})
    return render_to_response('book/search_form.html',{'errors': errors})

