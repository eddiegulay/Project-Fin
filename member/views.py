from django.shortcuts import render


def member_profile(request):
    return render(request, 'member/profile.html')