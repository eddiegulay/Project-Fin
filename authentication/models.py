from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Privilege(models.Model):
    privilege_name = models.CharField(max_length=50)

    def __str__(self):

        return self.privilege_name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    privilege = models.ForeignKey(Privilege, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.user.username

