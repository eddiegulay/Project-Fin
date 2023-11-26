from django.urls import path
from .views import *


urlpatterns = [
    path('', register_view, name='register'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', user_logout, name='logout'),

]


