from django.db import models
from userProfile.models import Profile
from django.contrib.auth.models import User

class Team(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    created = models.TimeField(auto_now_add=True)
    is_public = models.BooleanField(default=False)
    #team_join_code = models.BigIntegerField()
    #join_code_experi_date = models.TimeField()# TODO check this as well!
    #total_member = models.IntegerField(default=5)

#TODO should look into this OneToOneField etc.!
class TeamMember(models.Model):
    team = models.OneToOneField(Team, on_delete=models.CASCADE)
    team_user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_team_leader = models.BooleanField(default=False)
