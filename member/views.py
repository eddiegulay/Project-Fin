from django.shortcuts import render
from .models import *

def member_profile(request):
    user = request.user
    bio = Bio.objects.get(user=user)
    projects = Project.objects.filter(members=user)


    # success rate for project compeltion
    success_rate = 0
    if projects.count() > 0:
        success_rate = (projects.filter(is_completed=True).count() / projects.count()) * 100

    context = {
        'bio': bio,
        'projects': projects,
        'project_count': projects.count(),
        'success_rate': success_rate,
    }
    return render(request, 'member/profile.html', context)