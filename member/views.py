from django.shortcuts import render
from .models import *
from bank.models import *

def member_profile(request):
    user = request.user
    bio = Bio.objects.get(user=user)
    projects = Project.objects.filter(members=user)
    challenges = Challenge.objects.filter(collaborators=user)

    # success rate for project compeltion
    success_rate = 0
    if projects.count() > 0:
        success_rate = (projects.filter(is_completed=True).count() / projects.count()) * 100

    # get all users who invited member to collaborate in a challenge
    invites = []
    for challenge in challenges:
        creator = challenge.created_by
        invites.append({
            'challenge': challenge,
            'creator': creator,
        })


    context = {
        'bio': bio,
        'projects': projects,
        'project_count': projects.count(),
        'success_rate': success_rate,
        'invites': invites,
        'challenges': challenges,
    }
    return render(request, 'member/profile.html', context)