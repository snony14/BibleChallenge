from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib.auth import logout

#TODO move this somewhere else as well
# Create your views here.
def login(request):
    return render(request, 'user/dashboard.html', dict())

def logout_user(request):
    logout(request)
    return redirect("/")


#TODO Things start here!!
@login_required(login_url='/login/')
def profile(request):
    '''
    Get all the query associated with the current user such as where they are in their
    current progress with respect to the team challenge, also if there are any other challenges
    '''
    return render(request, 'user/dashboard.html', dict())


@login_required(login_url='/login/')
def challenges(request):
    return render(request, "user/challenges.html", dict())

from team.models import TeamMember
@login_required(login_url='/login/')
def teams(request):
    user = request.user
    team_members = TeamMember.objects.filter(team_user=user)
    #teams = [t.team for t in team_members]
    context = {"team_members":team_members}
    return render(request, "user/teams.html", context)

@login_required(login_url='/login/')
def settings(request):
    return render(request, "user/settings.html", dict())


'''
Need decorator in order to know login in people and not logging in people!!
'''
