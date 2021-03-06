from django.shortcuts import render, render_to_response
from django.http.response import HttpResponse, HttpResponseRedirect
from contact.forms import ContactForm
#from blog.models import Book
"""
def contact(request):
    errors = []
    if request.method == 'POST':
        if not request.POST.get('subject', ''):
            errors.append('Enter a subject.')
        if not request.POST.get('message', ''):
            errors.append('Enter a message')
        if request.POST.get('email') and '@' not in request.POST['email']:
            errors.append('Enter a valid e_mail address.')
        if not errors:
            send_mail(
                request.POST['subject'],
                request.POST['message'],
                request.POST.get('email', 'noreply@exampe.com'),
                ['siteowner@emample.com'],            
            )
            return HttpResponseRedirect('/contact/thanks/')
    return render_to_response('contact_form.html',{
        'error': errors,
        'subject': request.POST.get('subject', ''),
        'message': request.POST.get('message', ''),
        'email': request.POST.get('email',''),
        })
"""

def contact(request):
    if request.method == 'POST':
            form = ContactForm(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                send_mail(
                    cd['subject'],
                    cd['message'],
                    cd.get('mail', 'noreplay@example.com'),
                    ['549303402@qq.com'],                    
                )
                return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm(
            initial = {'subject': 'I love your site!'}
        )
    return render_to_response('contact_form.html', {'form': form})