from django.shortcuts import render
from .models import *

# Create your views here.
def thematic_areas(request):
    thematic_areas = ThematicArea.objects.all()
    Challenges = Challenge.objects.all()

    # get all collaborators for each challenge
    collaborators = []
    for challenge in Challenges:
        challenge_collaborators = challenge.collaborators.all()
        for collaborator in challenge_collaborators:
            collaborators.append(collaborator)

    collaborators = list(set(collaborators))

    context = {
        'thematic_areas': thematic_areas,
        'Challenges': Challenges,
        'collaborators': collaborators,
    }
    return render(request, 'bank/thematic_areas.html', context)


def challenges(request, thematic_area_id):
    thematic_areas = ThematicArea.objects.all()
    thematic_area = ThematicArea.objects.get(id=thematic_area_id)
    challenges = Challenge.objects.filter(thematic_area=thematic_area)
    context = {
        'thematic_areas': thematic_areas,
        'challenges': challenges,
        'thematic_area': thematic_area,
    }
    return render(request, 'bank/thematic_areas.html', context)