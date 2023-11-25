from django.shortcuts import render
from .models import *

# Create your views here.
def thematic_areas(request):
    thematic_areas = ThematicArea.objects.all()
    Challenges = Challenge.objects.all()

    context = {
        'thematic_areas': thematic_areas,
        'Challenges': Challenges,
    }
    return render(request, 'bank/thematic_areas.html', context)