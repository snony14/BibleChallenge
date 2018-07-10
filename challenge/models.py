from django.db import models

# Create your models here.
class Team(models.Model):
    title = models.CharField(max_length=150)
    summary = models.TextField()
    created = models.TimeField(auto_now_add=True)
    #team_leader = models. connect to user
    #team_code = connect to user id
    #logo = models.ImageField()
    #is_public = models.Boolean() TODO if team is public then can join otherwise no!!
