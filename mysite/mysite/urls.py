"""mysite URL Configuration

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
from mysite import views

urlpatterns = patterns("",
    #(r'^admin/', include(admin.site.urls)),
    (r'^hello/$', views.hello ),
    #(r'^bad_search',bad_search)
    (r'^time/plus/(\d{1,2})/$', views.hours_ahead),
    (r'^date/plus/(?P<month>\d{2})/(?P<year>\d{4})/$', views.time),
)

