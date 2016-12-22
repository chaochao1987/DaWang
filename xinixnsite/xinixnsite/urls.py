from django.conf.urls import patterns, url, include
from xinixnsite.views import hello, current_datetime, hours_ahead, book_list, current_url_view, display_meta
from books.views import search_form, search
from django.contrib import admin
from contact.views import contact

admin.autodiscover()


urlpatterns = patterns('',
    (r'admin/', include(admin.site.urls)),
    ('^hello/$', hello),
    ('^date/$', current_datetime),
    (r'^url/$',current_url_view),
    (r'^display/$',display_meta),
    #(r'^search_form/$', search_form),
    (r'^time/plus/(\d{1,2})/$', hours_ahead),
    (r'search_form/$', search),
    (r'^contact/$',contact),
  
)
