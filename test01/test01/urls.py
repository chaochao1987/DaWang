from django.conf.urls import patterns, url, include
from blog.views import hello, date, hours_ahead, thanks, current_datetime

urlpatterns = patterns('',
    (r'^hello/$', hello),
    (r'^date/$', date),
    (r'^time/plus/(\d{1,2})/$', hours_ahead),
    (r'^thank/$', thanks),
    (r'^current_datetime/$', current_datetime),
)