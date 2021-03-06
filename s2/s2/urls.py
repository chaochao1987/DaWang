"""s2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import patterns, include, url
from django.contrib import admin
#from blog.views import hello, ua_display_good2, display_meta, search_form, search_form, bad_search, search, thanks
#from contact.views import contact
#from blog import views
#from books import views

#urlpatterns = [
#    url(r'^admin/', include(admin.site.urls)),
    
#]

urlpatterns = patterns("books.views",
    (r'^admin/', include(admin.site.urls)),
    (r'^search/$', 'search_form'),
    #(r'^bad_search',bad_search)
)
