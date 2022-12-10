from django.urls import path,include, re_path

from home.views import *
from car_dealer_portal import *
from customer_portal import *

urlpatterns = [
    re_path(r'^$',home_page),
]
