from django.urls import path
from .views import *


urlpatterns = [
    path('', member_profile, name='member_profile'),
]