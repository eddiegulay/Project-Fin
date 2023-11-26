from django.urls import path
from .views import *

urlpatterns = [
    path('', thematic_areas, name='thematic_areas'),
    path('<int:thematic_area_id>/challenges', challenges, name='challenges'),
]