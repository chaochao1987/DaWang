from django.conf.urls import patterns, url, include
from xinixnsite.views import hello, current_datetime, hours_ahead, latest_books


urlpatterns = patterns('',
    ('^hello/$', hello),
    ('^date/$', current_datetime),
    (r'^time/plus/(\d{1,2})/$', hours_ahead),
    (r'^latest/$', latest_books)
)
