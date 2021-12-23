from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields.related import ForeignKey


class User(AbstractUser):
    name = models.CharField(max_length=25, default='Username')
    last_name = models.CharField(max_length=25, default='', null=True)
    description = models.TextField(default='Description')
    image = models.TextField()
    
    def __str__(self):
        return self.name

class Score(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='scores')
    quiz = models.ForeignKey('quiz2.Quiz', on_delete=models.DO_NOTHING, related_name='scores')
    value = models.IntegerField(default=0)

    def __str__(self):
        return self.user
