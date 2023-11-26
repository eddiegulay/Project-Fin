from django.db import models
from django.contrib.auth.models import User
from bank.models import Challenge

class Bio(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    reg_number = models.CharField(max_length=20)
    programme = models.CharField(max_length=100)
    interests = models.TextField()
    linked_in = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    skills = models.TextField()
    languages = models.TextField()
    quote = models.TextField()

    def __str__(self):
        return self.user.username


class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    members = models.ManyToManyField(User, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    is_completed = models.BooleanField(default=False)
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title


class ProjectFile(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='files')
    file = models.FileField(upload_to='project_files/')
    description = models.TextField()
    uploaded_by = models.ForeignKey(Bio, on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.project.title} - {self.description}"