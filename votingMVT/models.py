from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Candidates(models.Model):
    name = models.CharField(max_length=25)
    party = models.CharField(max_length=30)
    symbol = models.CharField(max_length=25)
    img = models.ImageField(upload_to='pics')
class UserVote(models.Model):
    isVoted = models.BooleanField(default=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    votedto = models.CharField(max_length=30)

