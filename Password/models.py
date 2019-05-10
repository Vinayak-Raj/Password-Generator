from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Password(models.Model):
    text = models.CharField(max_length=50)
    strength = models.BooleanField(default=False)

    def __str__(self):
        return self.text + ' | ' + str(self.strength)