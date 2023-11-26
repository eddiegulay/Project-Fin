from django.db import models
from member.models import User

class ThematicArea(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Challenge(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    thematic_area = models.ForeignKey(ThematicArea, on_delete=models.CASCADE)
    skills_required = models.CharField(max_length=200)
    programming_languages = models.CharField(max_length=200)
    collaborators = models.ManyToManyField(User, related_name='collaborations', blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_challenges')

    def __str__(self):
        return self.title
