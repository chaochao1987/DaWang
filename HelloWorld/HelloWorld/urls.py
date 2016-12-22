from django.conf.urls import patterns, include, url
from HelloWorld.view import current_datetime

urlpatterns = patterns("",
    ('^date$', current_datetime),
    ('^app1/', include('app1.urls')),
)
