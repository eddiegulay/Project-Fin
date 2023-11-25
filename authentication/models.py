from django.db import models


# Create your models here.

class privilege(models.Model):
    privilege_name = models.CharField(max_length=50)

    def __str__(self):

        return self.privilege_name


class Profile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    privilege = models.ForeignKey(privilege, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.user.username

