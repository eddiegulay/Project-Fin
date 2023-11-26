from django.shortcuts import render
from .models import *
from member.models import User, Project

# Create your views here.
def thematic_areas(request):
    thematic_areas = ThematicArea.objects.all()
    Challenges = Challenge.objects.all()

    # get my projects
    my_projects = []
    all_projects = Project.objects.all()
    for project in all_projects:
        try:
            if project.challenge.created_by == request.user:
                my_projects.append(project)
        except:
            pass


    # get all collaborators for each challenge
    collaborators = []
    for challenge in Challenges:
        challenge_collaborators = challenge.collaborators.all()
        for collaborator in challenge_collaborators:
            collaborators.append(collaborator)

    collaborators = list(set(collaborators))

    context = {
        'thematic_areas': thematic_areas,
        'challenges': Challenges,
        'collaborators': collaborators,
        'thematic_area':'',
        'projects': my_projects,
        'project_count': len(my_projects),
    }
    return render(request, 'bank/thematic_areas.html', context)


def challenges(request, thematic_area_id):
    thematic_areas = ThematicArea.objects.all()
    thematic_area = ThematicArea.objects.get(id=thematic_area_id)
    challenges = Challenge.objects.filter(thematic_area=thematic_area)

    # get my projects
    my_projects = []
    all_projects = Project.objects.all()
    for project in all_projects:
        try:
            if project.challenge.created_by == request.user:
                my_projects.append(project)
        except:
            pass


    # get all collaborators for each challenge
    collaborators = []
    for challenge in challenges:
        challenge_collaborators = challenge.collaborators.all()
        for collaborator in challenge_collaborators:
            collaborators.append(collaborator)

    collaborators = list(set(collaborators))

    context = {
        'thematic_areas': thematic_areas,
        'challenges': challenges,
        'thematic_area': thematic_area,
        'collaborators': collaborators,
        'projects': my_projects,
        'project_count': len(my_projects),
    }
    return render(request, 'bank/thematic_areas.html', context)