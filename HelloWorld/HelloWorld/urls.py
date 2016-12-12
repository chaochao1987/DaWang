from django.conf.urls import *
from HelloWorld.view import current_datetime

urlpatterns = patterns("",
    ('^date$', current_datetime),
)
