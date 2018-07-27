from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
# Create your views here.
@login_required(login_url='/login/')
def create_team(request):
    #TODO do validation for this part here!!
    title = request.POST.get("title", "")
    description = request.POST.get("textarea", "")
    is_public = request.POST.get("status", False)
    members = request.POST.get("members", 5)
    is_public = True if is_public=='on' else False
    team = Team(title=title,
          description=description,
          is_public=is_public)
    team.save()
    user = request.user
    team_member = TeamMember(team=team, team_user= user, is_team_leader=True)
    team_member.save()
    return redirect("/account/teams")
