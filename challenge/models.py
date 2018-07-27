from django.db import models
from team.models import Team, TeamMember

class Challenge(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    team = models.ForeignKey(Team,on_delete=models.CASCADE)#associated with the team
    created_by = models.ForeignKey(TeamMember, on_delete=models.SET_NULL, null=True)
    start_date = models.DateField()
    end_date = models.DateField()

class MemberChallenge(models.Model):
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE)
    team_member = models.ForeignKey(TeamMember, on_delete=models.CASCADE)
    progress = models.TextField()#TODO but before saving this, it should be turn to a json string and then be saved; all the checkpoint
    current_pos = models.IntegerField(default=0)#TODO there should be a constraint on the total number of current_pos


class CheckPoint(models.Model):
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE)
    goal = models.CharField(max_length=200)#TODO change this to include the bible verses instead or books
    description = models.TextField()#TODO might remove this one here


class Comment(models.Model):
    checkPoint = models.ForeignKey(CheckPoint, on_delete=models.CASCADE, related_name='comments')
    team_member = models.ForeignKey(TeamMember, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now=True)
